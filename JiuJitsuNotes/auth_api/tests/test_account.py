from django.test import TestCase

from .base_cases import AuthenticatingBaseTestCase


class TestAccount(AuthenticatingBaseTestCase):
    fixtures = [
        "users.json",
    ]

    def test_get(self):
        response = self.client.get(
            "/auth/account",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "username": "testUser",
            },
        )

    def test_post_good_credentials(self):
        """Tests that a new user can be created with a POST request, and then logged in via token."""
        response = self.client.post(
            "/auth/account",
            {
                "username": "newUsername",
                "password": "newPassword",
            },
        )

        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(
            response.json(),
            {
                "id": 2,
                "username": "newUsername",
            },
        )

        token_response = self.client.post(
            "/auth/token",
            {
                "username": "newUsername",
                "password": "newPassword",
            },
        )

        self.assertEqual(token_response.status_code, 200)
        self.assertIn("token", token_response.json())

    def test_post_bad_credentials(self):
        """Tests that a new user cannot be created with a POST request if the username already exists."""
        response = self.client.post(
            "/auth/account",
            {
                "username": "testUser",
                "password": "newPassword",
            },
        )

        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(
            response.json(),
            {
                "error": "username already exists",
            },
        )

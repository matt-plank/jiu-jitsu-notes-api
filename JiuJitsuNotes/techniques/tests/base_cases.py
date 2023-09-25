from django.test import TestCase


class AuthenticatingBaseTestCase(TestCase):
    def setUp(self):
        response = self.client.post(
            "/auth/token",
            {
                "username": "testUser",
                "password": "testPassword",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

        self.token = response.json()["token"]
        self.authorization = f"Token {self.token}"

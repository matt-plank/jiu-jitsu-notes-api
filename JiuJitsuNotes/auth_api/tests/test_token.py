from django.test import TestCase


class TestToken(TestCase):
    fixtures = [
        "users.json",
    ]

    def test_good_credentials(self):
        response = self.client.post(
            "/auth/token",
            {
                "username": "testUser",
                "password": "testPassword",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.json())

    def test_bad_credentials(self):
        response = self.client.post(
            "/auth/token",
            {
                "username": "testUser",
                "password": "badPassword",
            },
        )

        self.assertEqual(response.status_code, 401)
        self.assertDictEqual(response.json(), {"error": "invalid credentials"})

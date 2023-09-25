from .. import models
from .base_cases import AuthenticatingBaseTestCase


class TestGrip(AuthenticatingBaseTestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
        "users.json",
    ]

    def test_get(self):
        response = self.client.get("/api/grips/", HTTP_AUTHORIZATION=self.authorization)

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "name": "Pinch Headlock",
                },
                {
                    "id": 2,
                    "name": "Shoulder Crunch",
                },
            ],
        )

    def test_put(self):
        response = self.client.put(
            "/api/grips/",
            data={
                "id": 1,
                "name": "TEST GRIP",
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "name": "TEST GRIP",
            },
        )

    def test_post(self):
        response = self.client.post(
            "/api/grips/",
            data={
                "name": "MY TEST GRIP",
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json(),
            {
                "id": 3,
                "name": "MY TEST GRIP",
            },
        )

    def test_delete(self):
        response = self.client.delete(
            "/api/grips/",
            data={
                "id": 1,
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(models.Grip.objects.count(), 1)

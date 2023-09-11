from typing import Any

from django.test import TestCase
from rest_framework.test import APIClient


class TestRandomTechnique(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
    ]

    def test_get(self):
        response = self.client.get("/api/technique/random/")

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "name": "Move to Shoulder Crunch",
                "from_position": {
                    "name": "Closed Guard",
                    "your_grips": ["Pinch Headlock"],
                    "their_grips": [],
                    "aspect": "Playing",
                },
                "to_position": {
                    "name": "Closed Guard",
                    "your_grips": ["Shoulder Crunch"],
                    "their_grips": [],
                    "aspect": "Playing",
                },
            },
        )


class TestPositions(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
    ]

    def test_get(self):
        response = self.client.get("/api/position/")

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            response.json(),
            [
                {
                    "name": "Closed Guard",
                    "display_name": "Playing Closed Guard (Pinch Headlock)",
                    "your_grips": ["Pinch Headlock"],
                    "their_grips": [],
                    "aspect": "Playing",
                    "techniques": ["Move to Shoulder Crunch"],
                    "submissions": [],
                },
                {
                    "name": "Closed Guard",
                    "display_name": "Playing Closed Guard (Shoulder Crunch)",
                    "your_grips": ["Shoulder Crunch"],
                    "their_grips": [],
                    "aspect": "Playing",
                    "techniques": [],
                    "submissions": ["Ude Gatame"],
                },
            ],
        )


class TestGrip(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
    ]

    def test_get(self):
        response = self.client.get("/api/grips/")

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
        client = APIClient()
        response: Any = client.put(
            "/api/grips/",
            data={
                "id": 1,
                "name": "TEST GRIP",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "name": "TEST GRIP",
            },
        )

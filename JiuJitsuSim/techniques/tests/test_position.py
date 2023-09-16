from typing import Any

from django.test import TestCase
from rest_framework.test import APIClient


class TestPositions(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
    ]

    def test_get(self):
        response = self.client.get("/api/position/")

        self.maxDiff = 1000000

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "aspect": "Playing",
                    "name": "Closed Guard",
                    "display_name": "Playing Closed Guard (Pinch Headlock)",
                    "your_grips": [
                        {
                            "id": 1,
                            "name": "Pinch Headlock",
                        }
                    ],
                    "their_grips": [],
                    "techniques": [
                        {
                            "id": 1,
                            "name": "Move to Shoulder Crunch",
                            "to_position": {
                                "id": 2,
                                "aspect": "Playing",
                                "name": "Closed Guard",
                                "display_name": "Playing Closed Guard (Shoulder Crunch)",
                                "your_grips": [
                                    {
                                        "id": 2,
                                        "name": "Shoulder Crunch",
                                    },
                                ],
                                "their_grips": [],
                            },
                        }
                    ],
                    "submissions": [],
                },
                {
                    "id": 2,
                    "aspect": "Playing",
                    "name": "Closed Guard",
                    "display_name": "Playing Closed Guard (Shoulder Crunch)",
                    "your_grips": [
                        {
                            "id": 2,
                            "name": "Shoulder Crunch",
                        }
                    ],
                    "their_grips": [],
                    "techniques": [],
                    "submissions": [
                        {
                            "id": 1,
                            "name": "Ude Gatame",
                        }
                    ],
                },
            ],
        )

    def test_put(self):
        self.maxDiff = 1000000

        client = APIClient()

        response: Any = client.put(
            "/api/position/",
            data={
                "id": 1,
                "name": "New Position Name",
                "their_grips": [
                    "Pinch Headlock",
                ],
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "aspect": "Playing",
                "name": "New Position Name",
                "display_name": "Playing New Position Name (Pinch Headlock) vs (Pinch Headlock)",
                "your_grips": [
                    {
                        "id": 1,
                        "name": "Pinch Headlock",
                    }
                ],
                "their_grips": [
                    {
                        "id": 1,
                        "name": "Pinch Headlock",
                    }
                ],
                "techniques": [
                    {
                        "id": 1,
                        "name": "Move to Shoulder Crunch",
                        "to_position": {
                            "id": 2,
                            "aspect": "Playing",
                            "name": "Closed Guard",
                            "display_name": "Playing Closed Guard (Shoulder Crunch)",
                            "your_grips": [
                                {
                                    "id": 2,
                                    "name": "Shoulder Crunch",
                                }
                            ],
                            "their_grips": [],
                        },
                    }
                ],
                "submissions": [],
            },
        )

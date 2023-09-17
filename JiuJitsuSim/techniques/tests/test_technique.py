from django.test import TestCase


class TestRandomTechnique(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
    ]

    def test_get(self):
        self.maxDiff = 1000000

        response = self.client.get("/api/technique/random/")

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "name": "Move to Shoulder Crunch",
                "notes": "",
                "from_position": {
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
                },
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
            },
        )


class TestTechnique(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
    ]

    def test_put(self):
        response = self.client.put(
            "/api/technique/",
            data={
                "id": 1,
                "name": "New Technique Name",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "name": "New Technique Name",
                "notes": "",
                "from_position": {
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
                },
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
            },
        )

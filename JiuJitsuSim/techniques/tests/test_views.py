from django.test import TestCase


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

from django.test import TestCase

from ..models import SubmissionTechnique


class TestPositions(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
    ]

    maxDiff = 100000

    def test_put(self):
        response = self.client.put(
            "/api/submission/",
            data={
                "id": 1,
                "name": "New Submission Name",
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "name": "New Submission Name",
                "notes": "",
                "from_position": {
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

    def test_post(self):
        response = self.client.post(
            "/api/submission/",
            data={
                "name": "New Pinch Headlock Technique",
                "from_position": {
                    "id": 1,
                },
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 2,
                "name": "New Pinch Headlock Technique",
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
            },
        )

    def test_delete(self):
        response = self.client.delete(
            "/api/submission/",
            data={
                "id": 1,
            },
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(SubmissionTechnique.objects.count(), 0)

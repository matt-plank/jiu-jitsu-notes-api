from django.test import TestCase


class TestPlaylist(TestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
        "playlists.json",
    ]

    maxDiff = None

    def test_get_many(self):
        response = self.client.get("/api/playlists/")

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            response.json(),
            [
                {
                    "id": 1,
                    "name": "Shoulder Crunch",
                    "description": "Shoulder crunch playlist",
                    "positions": [
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
                        },
                    ],
                },
            ],
        )

    def test_get_single(self):
        response = self.client.get("/api/playlists/?id=1")

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 1,
                "name": "Shoulder Crunch",
                "description": "Shoulder crunch playlist",
                "positions": [
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
                    },
                ],
            },
        )

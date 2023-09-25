from typing import Any

from .. import models
from .base_cases import AuthenticatingBaseTestCase


class TestPositions(AuthenticatingBaseTestCase):
    fixtures = [
        "grips.json",
        "positions.json",
        "techniques.json",
        "submission_techniques.json",
        "playlists.json",
        "users.json",
    ]

    maxDiff = 1000000

    def test_get_single(self):
        response = self.client.get(
            "/api/position/?id=1",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
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
                "playlists": [],
            },
        )

    def test_get_many(self):
        response = self.client.get(
            "/api/position/",
            HTTP_AUTHORIZATION=self.authorization,
        )

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
                    "playlists": [],
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
                    "playlists": [
                        {
                            "id": 1,
                            "name": "Shoulder Crunch",
                            "description": "Shoulder crunch playlist",
                        }
                    ],
                },
            ],
        )

    def test_put(self):
        response: Any = self.client.put(
            "/api/position/",
            data={
                "id": 1,
                "name": "New Position Name",
                "their_grips": [
                    {
                        "id": 1,
                    }
                ],
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
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
                "playlists": [],
            },
        )

    def test_put_no_id(self):
        response = self.client.put(
            "/api/position/",
            data={
                "name": "New Position Name",
                "their_grips": [
                    {
                        "id": 1,
                    }
                ],
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 400)

    def test_put_no_grip_id(self):
        response = self.client.put(
            "/api/position/",
            data={
                "name": "New Position Name",
                "their_grips": [
                    {
                        "name": "Pinch Headlock",
                    }
                ],
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 400)

    def test_post(self):
        response = self.client.post(
            "/api/position/",
            data={
                "aspect": "Playing",
                "name": "New Position Name",
                "your_grips": [
                    {
                        "id": 1,
                    }
                ],
                "their_grips": [],
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.json(),
            {
                "id": 3,
                "aspect": "Playing",
                "name": "New Position Name",
                "display_name": "Playing New Position Name (Pinch Headlock)",
                "your_grips": [
                    {
                        "id": 1,
                        "name": "Pinch Headlock",
                    },
                ],
                "their_grips": [],
                "techniques": [],
                "submissions": [],
                "playlists": [],
            },
        )

    def test_post_no_name(self):
        response = self.client.post(
            "/api/position/",
            data={
                "aspect": "Playing",
                "your_grips": [
                    {
                        "id": 1,
                    }
                ],
                "their_grips": [],
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(models.Position.objects.count(), 2)

    def test_post_no_grip_id(self):
        response = self.client.post(
            "/api/position/",
            data={
                "aspect": "Playing",
                "name": "New Position Name",
                "your_grips": [
                    {
                        "name": "Pinch Headlock",
                    }
                ],
                "their_grips": [],
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(models.Position.objects.count(), 2)

    def test_post_no_aspect(self):
        response: Any = self.client.post(
            "/api/position/",
            data={
                "name": "My New Position",
                "your_grips": [
                    {
                        "id": 1,
                    }
                ],
                "their_grips": [],
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(models.Position.objects.count(), 2)

    def test_delete(self):
        delete_response = self.client.delete(
            "/api/position/",
            data={
                "id": 1,
            },
            content_type="application/json",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(delete_response.status_code, 200)

        response = self.client.get(
            "/api/position/",
            HTTP_AUTHORIZATION=self.authorization,
        )

        self.assertEqual(response.status_code, 200)
        self.assertListEqual(
            response.json(),
            [
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
                    "playlists": [
                        {
                            "id": 1,
                            "name": "Shoulder Crunch",
                            "description": "Shoulder crunch playlist",
                        }
                    ],
                },
            ],
        )

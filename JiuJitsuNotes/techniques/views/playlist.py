from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response

from ..models import Playlist, Position
from ..serializers import playlist as playlist_serializers


class PlaylistView(APIView):
    """View for interacting with the grip model."""

    permission_classes = [IsAuthenticated]

    def get_single(self, request):
        """GET a single playlist."""
        id: int = request.query_params["id"]
        playlist: Playlist = Playlist.objects.get(pk=id)

        result = playlist_serializers.CompleteSerializer(playlist).data

        return Response(result)

    def get_many(self, request):
        """GET all playlists."""
        playlists = Playlist.objects.all()
        result = playlist_serializers.CompleteSerializer(playlists, many=True).data

        return Response(result)

    def get(self, request):
        """Handle GET request. Return either a single playlist or a list of playlists depending on URL args."""
        if "id" in request.query_params:
            return self.get_single(request)

        return self.get_many(request)

    def put(self, request):
        """Handle PUT request. Update an existing playlist."""
        if "id" not in request.data:
            return Response({"error": "id not provided"}, status=400)

        playlist: Playlist = Playlist.objects.get(pk=request.data["id"])

        if "name" in request.data:
            playlist.name = request.data["name"]

        if "description" in request.data:
            playlist.description = request.data["description"]

        if "positions" in request.data:
            playlist.positions.clear()
            for position_data in request.data["positions"]:
                position_id: int = position_data["id"]
                position: Position = Position.objects.get(pk=position_id)
                playlist.positions.add(position)

        result = playlist_serializers.CompleteSerializer(playlist).data

        return Response(result)

    def post(self, request):
        """Handle POST request. Create a new playlist."""
        if "name" not in request.data:
            return Response({"error": "name not provided"}, status=400)

        if "description" not in request.data:
            return Response({"error": "description not provided"}, status=400)

        playlist: Playlist = Playlist.objects.create(
            name=request.data["name"],
            description=request.data["description"],
        )

        for position_data in request.data.get("positions", []):
            position_id: int = position_data["id"]
            position: Position = Position.objects.get(pk=position_id)
            playlist.positions.add(position)

        result = playlist_serializers.CompleteSerializer(playlist).data

        return Response(result)

    def delete(self, request):
        """Handle DELETE request. Delete a playlist."""
        if "id" not in request.data:
            return Response({"error": "id not provided"}, status=400)

        playlist: Playlist = Playlist.objects.get(pk=request.data["id"])
        playlist.delete()

        return Response(status=200)

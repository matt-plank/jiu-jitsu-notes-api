from rest_framework.views import APIView, Response

from .. import models
from ..serializers import playlist as playlist_serializers


class PlaylistView(APIView):
    """View for interacting with the grip model."""

    def get_single(self, request):
        """GET a single playlist."""
        id: int = request.query_params["id"]
        playlist: models.Playlist = models.Playlist.objects.get(pk=id)

        result = playlist_serializers.CompleteSerializer(playlist).data

        return Response(result)

    def get_many(self, request):
        """GET all playlists."""
        playlists = models.Playlist.objects.all()
        result = playlist_serializers.CompleteSerializer(playlists, many=True).data

        return Response(result)

    def get(self, request):
        """Handle GET request. Return either a single playlist or a list of playlists depending on URL args."""
        if "id" in request.query_params:
            return self.get_single(request)

        return self.get_many(request)

from django.contrib.auth.models import User

from ..models import Playlist


def all(user: User) -> Playlist:
    """Retrieve all playlists from the database for a given user."""
    return user.playlists.all()  # type: ignore


def find_by_id(user: User, id: int) -> Playlist:
    return user.playlists.get(pk=id)  # type: ignore


def create(user: User, name: str, description: str) -> Playlist:
    return Playlist.objects.create(
        user=user,
        name=name,
        description=description,
    )

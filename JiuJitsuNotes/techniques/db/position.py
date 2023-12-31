from django.contrib.auth.models import User

from ..models import Position


def find_by_id(user: User, id: int) -> Position:
    return user.positions.get(pk=id)  # type: ignore


def all(user: User, order_by=None):
    """Retrieve all positions from the database."""
    return user.positions.all().order_by(order_by) if order_by else user.positions.all()  # type: ignore


def create(user: User, name: str, aspect: str) -> Position:
    """Create a new position associated with a given user."""
    return Position.objects.create(
        user=user,
        name=name,
        aspect=aspect,
    )

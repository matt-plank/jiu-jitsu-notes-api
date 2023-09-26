import random

from django.contrib.auth.models import User

from ..models import Position, Technique


def find_by_id(user: User, id: int) -> Technique:
    return user.techniques.get(pk=id)  # type: ignore


def get_random(user: User) -> Technique:
    """Retrieve a random technique from the database."""
    total_techniques: int = user.techniques.count()  # type: ignore
    random_index = random.randint(0, total_techniques - 1)
    random_technique: Technique = Technique.objects.all()[random_index]

    return random_technique


def create(user: User, name: str, from_position: Position, to_position: Position) -> Technique:
    """Create a new technique associated with a given user."""
    return Technique.objects.create(
        user=user,
        name=name,
        from_position=from_position,
        to_position=to_position,
    )

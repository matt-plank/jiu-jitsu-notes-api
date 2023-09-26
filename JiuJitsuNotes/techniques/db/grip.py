from django.contrib.auth.models import User

from ..models import Grip


def all(user: User) -> Grip:
    """Retrieve all grips from the database."""
    return user.grips.all()  # type: ignore


def find_by_id(user: User, id: int) -> Grip:
    return user.grips.get(pk=id)  # type: ignore


def find_by_name(user: User, name: str) -> Grip:
    return user.grips.get(name=name)  # type: ignore


def delete_by_id(user: User, id: int):
    grip = user.grips.get(pk=id)  # type: ignore
    grip.delete()


def create(user: User, name: str) -> Grip:
    return Grip.objects.create(
        user=user,
        name=name,
    )

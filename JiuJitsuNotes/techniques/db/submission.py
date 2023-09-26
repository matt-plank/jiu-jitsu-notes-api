import random

from django.contrib.auth.models import User

from ..models import Position, SubmissionTechnique


def get_random(user: User) -> SubmissionTechnique:
    """Retrieve a random technique from the database."""
    total_submissions: int = user.submissions.count()  # type: ignore
    random_index = random.randint(0, total_submissions - 1)
    random_submission: SubmissionTechnique = SubmissionTechnique.objects.all()[random_index]

    return random_submission


def find_by_id(user: User, id: int) -> SubmissionTechnique:
    return user.submissions.get(pk=id)  # type: ignore


def create(user: User, name: str, from_position: Position) -> SubmissionTechnique:
    """Create a new submission associated with a given user."""
    return SubmissionTechnique.objects.create(
        user=user,
        name=name,
        from_position=from_position,
    )

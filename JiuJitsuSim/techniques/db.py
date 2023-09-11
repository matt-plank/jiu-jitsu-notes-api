import random

from .models import Grip, Position, SubmissionTechnique, Technique


def random_technique() -> Technique:
    """Retrieve a random technique from the database."""
    total_techniques: int = Technique.objects.count()
    random_index = random.randint(0, total_techniques - 1)
    random_technique: Technique = Technique.objects.all()[random_index]

    return random_technique


def random_submission() -> SubmissionTechnique:
    """Retrieve a random technique from the database."""
    total_submissions: int = SubmissionTechnique.objects.count()
    random_index = random.randint(0, total_submissions - 1)
    random_submission: SubmissionTechnique = SubmissionTechnique.objects.all()[random_index]

    return random_submission


def all_positions():
    """Retrieve all positions from the database."""
    positions = Position.objects.all()
    return positions


def all_grips():
    """Retrieve all grips from the database."""
    grips = Grip.objects.all()
    return grips


def find_grip(id: int) -> Grip:
    grip = Grip.objects.filter(id=id).first()

    if grip is None:
        raise ValueError(f"No grip found with id {id!r}")

    return grip


def delete_grip(id: int):
    grip = Grip.objects.filter(id=id).first()

    if grip is None:
        raise ValueError(f"No grip found with id {id!r}")

    grip.delete()

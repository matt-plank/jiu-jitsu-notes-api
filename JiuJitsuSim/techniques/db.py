import random

from .models import SubmissionTechnique, Technique


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

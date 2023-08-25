import random

from .models import Technique


def random_technique() -> Technique:
    """Retrieve a random technique from the database."""
    total_techniques: int = Technique.objects.count()
    random_index = random.randint(0, total_techniques - 1)
    random_technique: Technique = Technique.objects.all()[random_index]

    return random_technique

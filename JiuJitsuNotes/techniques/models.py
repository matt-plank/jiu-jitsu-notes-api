from django.contrib.auth.models import User
from django.db import models


def grip_names_list(grips) -> str:
    """Given a query of grips, list them as a comma-separated string."""
    grip_names: list[str] = [grip.name for grip in grips.all()]
    return ", ".join(grip_names)


def grips_versus(your_grips: str, their_grips: str) -> str:
    """Conditionally formatted string for two comma-separated lists of grips."""
    if your_grips == "" and their_grips == "":
        return ""

    if your_grips == "":
        return f"vs ({their_grips})"

    if their_grips == "":
        return f"({your_grips})"

    return f"({your_grips}) vs ({their_grips})"


class Grip(models.Model):
    """Represents a "grip" jiu-jitsu concept."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="grips",
    )

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class PositionDetail(models.TextChoices):
    """Options for how positions are played (either attacking, defending, etc)."""

    TOP_PIN = "Top"
    BOTTOM_PIN = "Bottom"
    ATTACKING_GUARD = "Passing"
    PLAYING_GUARD = "Playing"
    SUBMISSION = "Submission"


class Position(models.Model):
    """Represents a "position" jiu-jitsu concept. Behaves as a node on a directed graph."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="positions",
    )

    name = models.CharField(max_length=128)
    your_grips = models.ManyToManyField(Grip, related_name="your_grips", blank=True)
    their_grips = models.ManyToManyField(Grip, related_name="their_grips", blank=True)
    aspect = models.CharField(max_length=128, choices=PositionDetail.choices)

    def __str__(self):
        your_grips: str = grip_names_list(self.your_grips)
        their_grips: str = grip_names_list(self.their_grips)

        return f"{self.aspect} {self.name} {grips_versus(your_grips, their_grips)}"


class Technique(models.Model):
    """Represents a "technique" jiu-jitsu concept. Behaves as an edge on a directed graph."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="techniques",
    )

    name = models.CharField(max_length=128)

    from_position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="techniques_from",
    )

    to_position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="techniques_to",
    )

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SubmissionTechnique(models.Model):
    """Represents a "submission" jiu-jitsu concept.

    Behaves as an edge on the directed graph, between a position and a conceptual "submission"
    position, which is not implemented but implied."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="submissions",
    )

    name = models.CharField(max_length=128)

    from_position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="submissions_from",
    )

    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Playlist(models.Model):
    """Represents a "playlist", a simple way of organising positions."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="playlists",
    )

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    positions = models.ManyToManyField(
        Position,
        related_name="playlists",
        blank=True,
    )

    def __str__(self):
        return self.name

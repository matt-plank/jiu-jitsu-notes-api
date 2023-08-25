from typing import Any

from django.db import models


def grip_names_list(grips) -> str:
    grip_names: list[str] = [grip.name for grip in grips.all()]
    return ", ".join(grip_names)


def grips_versus(first_grips: str, last_grips: str) -> str:
    if first_grips == "":
        return f"({last_grips})"

    if last_grips == "":
        return f"({first_grips})"

    return f"({first_grips}) vs ({last_grips})"


class Grip(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


class PositionDetail(models.TextChoices):
    TOP_PIN = "Top Pin"
    BOTTOM_PIN = "Bottom Pin"
    ATTACKING_GUARD = "Attacking Guard"
    PLAYING_GUARD = "Playing Guard"


class Position(models.Model):
    name = models.CharField(max_length=128)
    your_grips = models.ManyToManyField(Grip, related_name="your_grips", blank=True)
    their_grips = models.ManyToManyField(Grip, related_name="their_grips", blank=True)
    aspect = models.CharField(max_length=128, choices=PositionDetail.choices)

    def __str__(self):
        your_grips: str = grip_names_list(self.your_grips)
        their_grips: str = grip_names_list(self.their_grips)

        return f"{self.name} [{self.aspect}] {grips_versus(your_grips, their_grips)}"


class Technique(models.Model):
    name = models.CharField(max_length=128)

    from_position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="from_position",
    )

    to_position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="to_position",
    )

    def __str__(self):
        return f"{self.from_position.name} => {self.name} => {self.to_position.name}"

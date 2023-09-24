from django.contrib import admin

from .models import Grip, Playlist, Position, SubmissionTechnique, Technique, grip_names_list


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("display_name", "your_grips_show", "their_grips_show")
    ordering = ("name", "aspect")
    search_fields = ("name", "aspect")

    def display_name(self, obj) -> str:
        return f"{obj.aspect} {obj.name}"

    def your_grips_show(self, obj) -> str:
        return grip_names_list(obj.your_grips.all())

    def their_grips_show(self, obj) -> str:
        return grip_names_list(obj.their_grips.all())


@admin.register(Technique)
class TechniqueAdmin(admin.ModelAdmin):
    list_display = ("name", "to_position", "from_position")
    ordering = ("from_position",)
    search_fields = (
        "name",
        "from_position__name",
        "from_position__your_grips__name",
        "from_position__their_grips__name",
    )
    list_filter = ("from_position",)


@admin.register(SubmissionTechnique)
class SubmissionTechniqueAdmin(admin.ModelAdmin):
    list_display = ("name", "from_position")
    ordering = ("from_position",)
    search_fields = (
        "name",
        "from_position__name",
        "from_position__your_grips__name",
        "from_position__their_grips__name",
    )
    list_filter = ("from_position",)


admin.site.register(Grip)
admin.site.register(Playlist)

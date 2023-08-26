from django.contrib import admin

from .models import Grip, Position, Technique, grip_names_list


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name", "aspect", "your_grips_show", "their_grips_show")
    ordering = ("name", "aspect")
    search_fields = ("name", "aspect")

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

    def from_position_string(self, obj) -> str:
        return str(obj.from_position)


admin.site.register(Grip)

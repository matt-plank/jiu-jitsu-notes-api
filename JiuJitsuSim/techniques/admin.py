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


admin.site.register(Technique)
admin.site.register(Grip)

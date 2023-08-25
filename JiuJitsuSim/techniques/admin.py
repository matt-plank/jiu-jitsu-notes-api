from django.contrib import admin

from .models import Grip, Position, Technique

admin.site.register(Position)
admin.site.register(Technique)
admin.site.register(Grip)

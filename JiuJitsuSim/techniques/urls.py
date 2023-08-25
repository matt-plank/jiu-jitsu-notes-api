from django.urls import path

from .views import RandomTechniqueView

urlpatterns = [
    path("technique/random/", RandomTechniqueView.as_view()),
]

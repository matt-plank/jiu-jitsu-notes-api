from django.urls import path

from .views import RandomSubmissionView, RandomTechniqueView

urlpatterns = [
    path("technique/random/", RandomTechniqueView.as_view()),
    path("submission/random/", RandomSubmissionView.as_view()),
]

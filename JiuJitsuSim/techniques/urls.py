from django.urls import path

from .views import PositionsView, RandomSubmissionView, RandomTechniqueView

urlpatterns = [
    path("position/", PositionsView.as_view()),
    path("technique/random/", RandomTechniqueView.as_view()),
    path("submission/random/", RandomSubmissionView.as_view()),
]

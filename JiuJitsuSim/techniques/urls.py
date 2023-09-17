from django.urls import path

from .views import grip, position, submission, technique

urlpatterns = [
    path("position/", position.PositionsView.as_view()),
    path("grips/", grip.GripView.as_view()),
    path("technique/random/", technique.RandomTechniqueView.as_view()),
    path("submission/random/", submission.RandomSubmissionView.as_view()),
]

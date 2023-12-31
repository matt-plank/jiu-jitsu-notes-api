from django.urls import path

from .views import grip, playlist, position, submission, technique

urlpatterns = [
    path("position/", position.PositionsView.as_view()),
    path("grips/", grip.GripView.as_view()),
    path("technique/", technique.TechniqueView.as_view()),
    path("submission/", submission.SubmissionView.as_view()),
    path("technique/random/", technique.RandomTechniqueView.as_view()),
    path("submission/random/", submission.RandomSubmissionView.as_view()),
    path("playlists/", playlist.PlaylistView.as_view()),
]

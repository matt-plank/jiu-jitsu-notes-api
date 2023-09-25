from django.urls import path

from . import views

urlpatterns = [
    path("token", views.TokenView.as_view()),
    path("account", views.AccountView.as_view()),
]

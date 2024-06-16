from django.urls import path, include

from users.views import authView, logout, home

urlpatterns = [
    path("", home, name="home"),
    path("accounts/logout/", logout, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="authView"),
]

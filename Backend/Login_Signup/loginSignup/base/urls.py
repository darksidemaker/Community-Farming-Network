from django.urls import path, include
from django.views.generic import TemplateView
from .views import authView, home

urlpatterns = [
    path("", home, name="home"),
    path('logout_view/',TemplateView.as_view(template_name='home.html'),name='logout_view',),
    path("signup/", authView, name="authView"),
    path("accounts/", include("django.contrib.auth.urls")),
]

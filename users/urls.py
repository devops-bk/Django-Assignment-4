from django.urls import path
from .views import Usersignupview

urlpatterns = [
    path("signup/", Usersignupview.as_view(), name="signup"),
]
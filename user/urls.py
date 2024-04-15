from django.urls import path
from . import views



urlpatterns = [
    path("register/", views.create_user_view, name="create_user"),
    path("login/", views.login_user_view, name="login_user"),
    path("edit-profile/", views.update_user_view, name="update_user")
]

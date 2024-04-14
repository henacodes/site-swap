from django.urls import path
from . import views


urlpatterns = [
    path("", views.site_list, name="site_list")
]

from django.urls import path
from . import views


urlpatterns = [
    path("", views.site_list, name="site_list"),
    path("add-site", views.create_site, name="create_site"),
    path("<int:site_id>/", views.site_details, name="site_details")
]

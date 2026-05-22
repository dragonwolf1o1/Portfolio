from django.urls import path, re_path

from . import views


app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("contact/", views.contact, name="contact"),
    path("error/404/", views.error_404, name="error_404"),
    path("error/500/", views.error_500, name="error_500"),
    re_path(r"^.*$", views.error_404, name="catch_all_404"),
]

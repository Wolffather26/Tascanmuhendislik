from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("projeler/", views.project_list, name="project_list"),
    path("projeler/<slug:slug>/", views.project_detail, name="project_detail"),
    path("iletisim/", views.contact, name="contact"),
]

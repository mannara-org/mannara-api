from django.urls import path

from . import views

urlpatterns = [
    path("collection/specialties", views.specialties),
    path("collection/semesters", views.semesters),
    path("collection/academicLevels", views.academicLevels),
]

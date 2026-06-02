from django.urls import path
from . import views

urlpatterns = [
    path("", views.create_booking, name="create_booking"),
    path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
]
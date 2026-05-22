from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_home, name="booking_home"),
    path("new/", views.create_booking, name="create_booking"),
    path("success/", views.booking_success, name="booking_success"),
]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.booking_home, name="booking_home"),   # /bookings/
    path("new/", views.create_booking, name="create_booking"),  # /bookings/new/
    path("success/", views.booking_success, name="booking_success"),  # /bookings/success/
]
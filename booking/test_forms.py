from django.test import TestCase
from .forms import BookingForm


class TestBookingForm(TestCase):

    def test_form_is_valid(self):

        form = BookingForm({
            "full_name": "John Smith",
            "email": "john@email.com",
            "phone": "07123456789",
            "booking_date": "2026-08-15",
            "booking_time": "18:00",
            "number_of_guests": 4,
            "message": "Window table please"
        })

        self.assertTrue(
            form.is_valid(),
            msg="Booking form should be valid"
        )

    def test_name_is_required(self):

        form = BookingForm({
            "full_name": "",
            "email": "john@email.com",
            "phone": "07123456789",
            "booking_date": "2026-08-15",
            "booking_time": "18:00",
            "number_of_guests": 4,
            "message": "Window table please"
        })

        self.assertFalse(
            form.is_valid(),
            msg="Form is valid when full_name is empty"
        )
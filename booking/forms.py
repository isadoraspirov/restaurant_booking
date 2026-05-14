from django import forms
from .models import BookingRequest


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = [
            "full_name",
            "email",
            "phone",
            "booking_date",
            "booking_time",
            "number_of_guests",
            "message",
        ]
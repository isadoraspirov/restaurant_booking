from django import forms
from .models import BookingRequest


class BookingForm(forms.ModelForm):

    booking_date = forms.DateField(
        input_formats=["%d/%m/%Y"],
        widget=forms.DateInput(
            attrs={
                "placeholder": "DD/MM/YYYY"
            }
        )
    )
    
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
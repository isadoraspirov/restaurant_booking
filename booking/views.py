from django.shortcuts import (
    render,
    get_object_or_404
)

from .forms import BookingForm
from .models import BookingRequest
from homepage.models import InfoRestaurant


def booking_home(request):
    return render(request, "booking/create_booking.html")


def create_booking(request):

    if request.method == "POST":

        form = BookingForm(request.POST)

        if form.is_valid():

            restaurant = InfoRestaurant.objects.first()

            booking = form.save(commit=False)
            booking.restaurant = restaurant
            booking.save()

            return render(
                request,
                "booking/booking_success.html",
                {
                    "booking": booking
                }
            )

    else:

        form = BookingForm()

    return render(
        request,
        "booking/create_booking.html",
        {
            "form": form,
            "editing": False,
        }
    )


def edit_booking(request, booking_id):

    booking = get_object_or_404(
        BookingRequest,
        id=booking_id
    )

    if request.method == "POST":

        form = BookingForm(
            request.POST,
            instance=booking
        )

        if form.is_valid():

            updated_booking = form.save()

            return render(
                request,
                "booking/booking_success.html",
                {
                    "booking": updated_booking
                }
            )

    else:

        form = BookingForm(instance=booking)

    return render(
        request,
        "booking/create_booking.html",
        {
            "form": form,
            "booking": booking,
            "editing": True,
        }
    )
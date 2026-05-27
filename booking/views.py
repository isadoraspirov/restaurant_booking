from django.shortcuts import render
from .forms import BookingForm
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
            "form": form
        }
    )
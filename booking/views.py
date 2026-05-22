from django.shortcuts import render, redirect
from .forms import BookingForm


def booking_home(request):
    return redirect("create_booking")


def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save()
            return render(request, "bookings/booking_success.html", {
                "booking": booking
            })

    else:
        form = BookingForm()

    return render(request, "bookings/create_booking.html", {"form": form})


def booking_success(request):
    return render(request, "bookings/booking_success.html")
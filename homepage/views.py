from django.shortcuts import render
from .models import InfoRestaurant

def home(request):
    restaurant = InfoRestaurant.objects.first()

    return render(request, "homepage/home.html", {
        "restaurant": restaurant
    })
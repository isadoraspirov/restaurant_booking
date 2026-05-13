from django.shortcuts import render
from .models import InfoRestaurant

# Create your views here.
def home(request):
    restaurant = InfoRestaurant.objects.first()

    context = {
        "restaurant": restaurant
    }

    return render(request, "homepage/home.html", context)
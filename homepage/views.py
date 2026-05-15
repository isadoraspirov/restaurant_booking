from django.shortcuts import render
from .models import InfoRestaurant

# Create your views here.
def index(request):
    restaurant = InfoRestaurant.objects.first()

    context = {
        "restaurant": restaurant
    }

    return render(request, "homepage/home.html", context)
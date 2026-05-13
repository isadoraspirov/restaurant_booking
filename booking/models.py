from django.db import models
from homepage.models import InfoRestaurant

# Create your models here.

class BookingRequest(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("rejected", "Rejected"),
    ]

    restaurant = models.ForeignKey(
        InfoRestaurant,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    booking_date = models.DateField()
    booking_time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()

    message = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.booking_date} {self.booking_time}"

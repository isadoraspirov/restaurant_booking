from django.test import TestCase
from django.urls import reverse

from homepage.models import InfoRestaurant


class TestBookingViews(TestCase):

    def setUp(self):

        self.restaurant = InfoRestaurant.objects.create(
            name="The Booking Table",
            address="123 High Street",
            city="Oxford",
            postcode="OX1 1AA",
            phone="07123456789",
            email="info@bookingtable.com"
        )

    def test_booking_page_loads(self):

        response = self.client.get(
            reverse("create_booking")
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_create_booking_success(self):

        response = self.client.post(
            reverse("create_booking"),
            {
                "full_name": "John Smith",
                "email": "john@email.com",
                "phone": "07123456789",
                "booking_date": "2026-08-15",
                "booking_time": "18:00",
                "number_of_guests": 4,
                "message": "Window table please"
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Booking Confirmed!"
        )
from django.urls import path
from bookings.views.Booking import Booking

ulrpatterns = [
    path(r'^booking/', Booking.as_view(), name='user')
]
from django.db import models
from .base_model import BaseModel


class Booking(BaseModel):
    user_id = models.IntegerField()
    trip_type = models.CharField(max_length=100)
    fromPlace = models.CharField(max_length=100)
    toPlace = models.CharField(max_length=100)
    returnTrip = models.BooleanField(default=False)
    passengers = models.IntegerField()
    currencyType = models.CharField(max_length=100)

    class Meta:
        db_table = 'bookings'
    

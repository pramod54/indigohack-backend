from django.db import models
from .base_model import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    active = models.BooleanField(deafult=True)

    class Meta:
        db_table = 'user'
        
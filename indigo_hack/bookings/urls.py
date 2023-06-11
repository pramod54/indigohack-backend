from django.urls import path
from bookings.views.user import User

ulrpatterns = [
    path(r'^user', User.as_view(), name='user')
]
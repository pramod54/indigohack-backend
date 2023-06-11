from indigo_hack.bookings.models.user import User
from indigo_hack.bookings.models.booking import Booking


class BookingController():

    def generate_booking_payload(self, data: dict, user_id:int) -> dict:
        return {
            "user_id":  user_id,
            "trip_type": data.get('trip_type'),
            "fromPlace": data.get('fromPlace'),
            "toPlace": data.get('toPlace'),
            "returnTrip": data.get('returnTrip', 0),
            "passengers": data.get('passengers'),
            "currencyType": data.get('currencyType')
        }

    def create_user_payload(self, data: dict) -> dict:
        return {
            "email_id": data.get('email_id'),
            "phone_number": data.get('phone_number')
        }

    def create_booking(self, data: dict) -> (dict, int, str):
        try:
            user_exists = User.objects.get(phone_number=data.get('phone_number'), email_id=data.get('email_id'))
            if user_exists.exists():
                booking_payload = self.generate_booking_payload(data=data, user_id=user_exists.id)
            else:
                user_payload = self.create_user_payload(data=data)
                user = User.objects.create(**user_payload)
                booking_payload = self.generate_booking_payload(data=data, user_id=user.id)
            booking = Booking.objects.create(**booking_payload)
            return booking, 0, "Booking created successfully."
        except Exception:
            return None, 1, "Booking creatio failed."

    def update_booking(self, data: dict) -> (dict, int, str):
        try:
            new_booking = Booking.objects.filter(id=data.get('booking_id')).update(**data)
            return new_booking, 0, "Booking update failed."
        except Exception:
            return None, 1, "Booking update failed."

    def get_user_booking(self, data: dict) -> (list, int, str):
        try:
            user = User.objects.get(email_id=data.get('email_id'), phone_number=data.get('phone_number'))
            if user.exists():
                bookings = Booking.objects.get(user_id=user.id)
                return bookings, 0, "User bookings success."
            else:
                return None, 1, "No user found. Please create one."
        except Exception:
            return None, 1, "Bad request."

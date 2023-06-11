from rest_framework import serializers, exceptions


class BookingSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if not (data.get('phone_number') or data.get('email_id')):
            return exceptions.APIException({
                "status": 1,
                "message": "Phone number and email id is required."
            })
        
        if not (data.get('fromPlace') or data.get('toPlace') or data.get('passengers') or data.get('currencyType')):
            return exceptions.APIException({
                "status": 1,
                "message": "Please fill all the mandatory fields."
            })
        return data

    def to_representation(self, data):
        return {
            "user_id": data.user_id,
            "fromPlace": data.fromPlace,
            "toPlace": data.fromPlace,
            "returnTrip": data.returnTrip,
            "passengers": data.passengers,
            "currency": data.currencyType
        }


class BookingUpdateSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        if (data.get('phone_number') or data.get('email_id')):
            return exceptions.APIException({
                "status": 1,
                "message": "Phone number and email id can be changed."
            })
        return data

    def to_representation(self, data):
        return {
            "user_id": data.user_id,
            "fromPlace": data.fromPlace,
            "toPlace": data.fromPlace,
            "returnTrip": data.returnTrip,
            "passengers": data.passengers,
            "currency": data.currencyType
        }

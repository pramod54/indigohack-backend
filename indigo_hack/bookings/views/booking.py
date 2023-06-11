from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bookings.serializers.booking import BookingSerializer,BookingUpdateSerializer
from bookings.controllers.booking import BookingController


class Booking(APIView):
    def post(self, request, *args, **kwargs):
        validator = BookingSerializer(data=request.data)
        validator.is_valid(raise_exceptions=True)
        validated_data = validator.validated_data
        
        data, status_code, msg = BookingController().create_booking(data=validated_data)

        if not data:
            return Response(
                {
                    "status": status_code,
                    "message": msg
                }, status=status.HTTP_404_NOT_FOUND
            )
        serialized_data = BookingSerializer(data).data
        return Response({
            "status": status_code,
            "message": msg,
            "data": serialized_data
        }, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        validator = BookingUpdateSerializer(data=request.data)
        validator.is_valid(raise_exceptions=True)
        validated_data = validator.validated_data

        data, status_code, msg = BookingController().update_booking(data=validated_data)

        if not data:
            return Response(
                {
                    "status": status_code,
                    "message": msg
                }, status=status.HTTP_404_NOT_FOUND
            )
        serialized_data = BookingUpdateSerializer(data).data
        return Response({
            "status": status_code,
            "message": msg,
            "data": serialized_data
        }, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        data, status_code, msg = BookingController().get_user_booking(data=request.data)
        if not data:
            return Response(
                {
                    "status": status_code,
                    "message": msg
                }, status=status.HTTP_404_NOT_FOUND
            )
        
        serializer_data = BookingSerializer(data, many=True).data
        return Response({
            "status": status_code,
            "message": msg,
            "data": serializer_data
        }, status=status.HTTP_200_OK)
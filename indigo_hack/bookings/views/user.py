from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class User(APIView):
    def post(self, request, *args, **kwargs):
        response = {"status": 1, "message": "Success"}
        return Response(response, status=status.HTTP_200_OK)
        
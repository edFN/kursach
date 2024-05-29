from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from notification_app.models import NotificationEmailRegister


# Create your views here.
class AcceptEmailRegister(APIView):
    class Validator(serializers.Serializer):
        email = serializers.EmailField(label="Email", allow_blank=False,
                                       allow_null=False)

    def post(self, request, *args, **kwargs):

        serializer = AcceptEmailRegister.Validator(data=request.data)

        serializer.is_valid(raise_exception=True)

        NotificationEmailRegister.objects.create(email=serializer.validated_data['email'])

        return Response(status=200)

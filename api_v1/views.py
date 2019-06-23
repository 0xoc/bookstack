from random import randint

from django.contrib.auth.models import User
from rest_framework import status

from rest_framework.generics import CreateAPIView
# Create your views here.
from rest_framework.response import Response

from api_v1.serializers import UserProfileGetOrCreate
from sms.models import Message, Operator
from users.models import UserProfile


class Login(CreateAPIView):
    serializer_class = UserProfileGetOrCreate

    allowed_methods = ['POST', ]

    def post(self, request, *args, **kwargs):
        the_serializer = self.serializer_class(data=request.data)

        if not the_serializer.is_valid():
            return Response({'errors': the_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        phone_number = request.data.get('phone_number', None)

        try:
            profile = UserProfile.objects.get(phone_number=phone_number)
            user = profile.user
        except UserProfile.DoesNotExist:
            user = User.objects.create(username=phone_number)
            profile = UserProfile.objects.create(user=user, phone_number=phone_number)

        password = randint(1000, 9999)

        user.set_password(password)

        message = Message(message="کلمه عبور یکبار مصرف بوک استک شما: %d" % password, to=phone_number)
        operator = Operator.objects.first()
        operator.send_message(message)
        return Response({"password": password})


from phoneaddressbook.models import PhoneInfo
from phoneaddressbook.serializers import PhoneInfoSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class PhoneInfoList(generics.ListCreateAPIView):
    queryset = PhoneInfo.objects.all()
    serializer_class = PhoneInfoSerializer
    
class PhoneInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PhoneInfo.objects.all()
    serializer_class = PhoneInfoSerializer
    
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

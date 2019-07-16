from phoneaddressbook.models import PhoneInfo
from phoneaddressbook.serializers import PhoneInfoSerializer, UserSerializer
from phoneaddressbook.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

class PhoneInfoViewSet(viewsets.ModelViewSet):
    queryset = PhoneInfo.objects.all()
    serializer_class = PhoneInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    

    def perform_create(self, phone_info):
        phone_info.save(owner = self.request.user)

    
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_list', request=request, format=format),
        'phone_info': reverse('phone_info_list', request=request, format=format)
    })

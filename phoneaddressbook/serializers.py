from rest_framework import serializers
from phoneaddressbook.models import PhoneInfo
from django.contrib.auth.models import User

class PhoneInfoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = PhoneInfo
        fields = ['url','id', 'first_name', 'last_name', 'relationship', 'mobile_number', 'landline_number', 'owner']
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    numbers = serializers.PrimaryKeyRelatedField(many=True, queryset=PhoneInfo.objects.all())
    
    class Meta:
        model = User
        fields = ['url', 'id', 'numbers', 'username']
        

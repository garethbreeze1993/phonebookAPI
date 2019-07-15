from rest_framework import serializers
from phoneaddressbook.models import PhoneInfo
from django.contrib.auth.models import User

class PhoneInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneInfo
        fields = ['id', 'first_name', 'last_name', 'relationship', 'mobile_number', 'landline_number']
        
class UserSerializer(serializers.ModelSerializer):
    numbers = serializers.PrimaryKeyRelatedField(many=True, queryset=PhoneInfo.objects.all())
    
    class Meta:
        model = User
        fields = ['id', 'numbers', 'username']
        

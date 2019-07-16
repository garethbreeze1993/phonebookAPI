from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from phoneaddressbook.views import PhoneInfoViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'phonenumbers', PhoneInfoViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
	path('', include(router.urls))
]


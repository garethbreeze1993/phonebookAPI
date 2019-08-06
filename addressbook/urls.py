from django.urls import path
from django.contrib.auth import views as auth_views # djangos built in auth
from addressbook import views

app_name = 'addressbook'

urlpatterns = [
    path('userlist/', views.UserList.as_view(), name='userlist'),
    path('usernumbers/<int:pk>', views.user_phone_numbers, name='usernumbers'),
    path('entry/<int:pk>/', views.PhoneInfoDetail.as_view(), name='phone_entry'),
	
]

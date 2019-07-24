from django.shortcuts import render

from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from phoneaddressbook.models import PhoneInfo

from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.models import User as u

class UserList(ListView):
	model = u
	
class UserPhoneNUmbers(ListView):
	model = PhoneInfo
	'''
	Logic to get each users addressbook and display on template
	'''
	
class PhoneInfoDetail(DetailView):
	model = PhoneInfo
	'''
	Should be all that is needed as just need to display a phone address book entry
	
	'''

from django.shortcuts import render

from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from phoneaddressbook.models import PhoneInfo
from django.http import Http404
from django.contrib.auth import get_user_model
Usera = get_user_model()

from django.contrib.auth.models import User as u

class UserList(ListView):
    
    model = u
    template_name = 'addressbook/user_list.html'
    context_object_name = 'user_list'
	
	
class PhoneInfoDetail(DetailView):
    model = PhoneInfo
    template_name = 'addressbook/phone_info_detail.html'
    context_object_name = 'phoneInfo'

    '''
	Should be all that is needed as just need to display a phone address book entry
	
    '''
    
def user_phone_numbers(request, pk):
        user_name = u.objects.get(pk=pk)
        phone_user = PhoneInfo.objects.filter(owner=user_name)
        
        return render(request, 'addressbook/user_phone_number.html', {'phone_user': phone_user})
        

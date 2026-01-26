from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomePage(TemplateView):
	"""
	Displays home page
	"""
	template_name = 'index.html'

class LoginViewCustom(LoginView):
	template_name = 'account/login.html'

class SignupView(CreateView):
	form_class = UserCreationForm
	template_name = 'account/signup.html'
	success_url = reverse_lazy('login')

def test_static(request):
	return render(request, 'test_static.html')

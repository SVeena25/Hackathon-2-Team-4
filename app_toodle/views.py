from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
	"""
	Displays home page
	"""
	template_name = 'index.html'

def test_static(request):
	return render(request, 'test_static.html')

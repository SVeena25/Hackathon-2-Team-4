import json
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Task
from django import forms


class HomePage(TemplateView):
	"""
	Displays home page or redirects to tasks if logged in
	"""
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('task_list')
		return super().get(request, *args, **kwargs)


# Task Views
class TaskListView(LoginRequiredMixin, ListView):
	model = Task
	template_name = 'task_list.html'
	context_object_name = 'tasks'
	login_url = 'account_login'

	def get_queryset(self):
		return Task.objects.filter(user=self.request.user)


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title']
		widgets = {
			'title': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter task title'
			})
		}


class TaskCreateView(LoginRequiredMixin, CreateView):
	model = Task
	form_class = TaskForm
	template_name = 'task_form.html'
	success_url = reverse_lazy('task_list')
	login_url = 'account_login'

	def form_valid(self, form):
		form.instance.user = self.request.user
		response = super().form_valid(form)
		messages.success(self.request, f'Task "{form.instance.title}" created successfully!')
		return response


class TaskUpdateView(LoginRequiredMixin, UpdateView):
	model = Task
	form_class = TaskForm
	template_name = 'task_form.html'
	success_url = reverse_lazy('task_list')
	login_url = 'account_login'

	def get_queryset(self):
		return Task.objects.filter(user=self.request.user)

	def form_valid(self, form):
		response = super().form_valid(form)
		messages.success(self.request, f'Task "{form.instance.title}" updated successfully!')
		return response


class TaskDeleteView(LoginRequiredMixin, DeleteView):
	model = Task
	template_name = 'task_delete.html'
	success_url = reverse_lazy('task_list')
	login_url = 'account_login'

	def get_queryset(self):
		return Task.objects.filter(user=self.request.user)

	def post(self, request, *args, **kwargs):
		task = self.get_object()
		task_title = task.title
		messages.error(request, f'Task "{task_title}" deleted successfully!')
		return super().post(request, *args, **kwargs)


@require_POST
def task_toggle_status(request, pk):
	try:
		task = Task.objects.get(pk=pk, user=request.user)
		data = json.loads(request.body)
		task.status = data.get('completed', False)
		task.save()
		return JsonResponse({'status': 'success', 'completed': task.status})
	except Task.DoesNotExist:
		return JsonResponse({'status': 'error', 'message': 'Task not found'}, status=404)
	except Exception as e:
		return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

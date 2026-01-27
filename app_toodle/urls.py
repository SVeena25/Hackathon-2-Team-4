
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('accounts/profile/', RedirectView.as_view(url='/tasks/', permanent=False), name='account_profile'),
    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(),
         name='task_create'),
    path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(),
         name='task_edit'),
    path('tasks/<int:pk>/delete/', views.TaskDeleteView.as_view(),
         name='task_delete'),
    path('tasks/<int:pk>/toggle/', views.task_toggle_status,
         name='task_toggle'),
    path('login/', RedirectView.as_view(url='/accounts/login/', permanent=False)),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('test-static/', views.test_static, name='test_static'),
]

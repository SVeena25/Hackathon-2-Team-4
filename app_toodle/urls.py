from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('test-static/', views.test_static, name='test_static'),
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
]

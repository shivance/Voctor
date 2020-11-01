from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

from . import views
urlpatterns = [
    path('',LoginView.as_view(template_name='usersApp/login.html'),name='login'),
    path('register/',views.register,name='register'),
    path('logout/', LogoutView.as_view(template_name='usersApp/login.html'),name='logout'),
]

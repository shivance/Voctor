from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('upload/',views.upload,name='upload'),
    path('find/',views.contact,name='contact'),
]


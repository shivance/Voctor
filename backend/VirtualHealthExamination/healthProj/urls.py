from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('upload/',views.upload,name='upload'),
    path('find/',views.find,name='find'),
    path('doctors/',views.doctors,name='doctors'),
    path('doctors/fullList/<specialisation>/',views.fullList,name='fullList'),
    path('doctors/appointment/<email>',views.appointment,name='appointment')
]

# the product is under production
# so DEBUG is true
# kindly don't share the secret key without permission

# Mohd Sufiyan Ansari
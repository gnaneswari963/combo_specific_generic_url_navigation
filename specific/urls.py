from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('employee/',employee,name='employee'),
    path('manager/',manager,name='manager'),
]
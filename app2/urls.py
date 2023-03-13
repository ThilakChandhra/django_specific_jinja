from app2.views import *
from django.urls import path

app_name='persons'

urlpatterns=[
    path('specific2/',specific2,name='specific2'),
]
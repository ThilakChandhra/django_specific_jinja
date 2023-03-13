from app1.views import *
from django.urls import path

app_name='special'

urlpatterns=[
    path('specific1/',specific1,name='specific1'),
]
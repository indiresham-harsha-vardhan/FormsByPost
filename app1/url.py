from django.urls import path
from .views import *
app_name='app1'

urlpatterns=[
    path('form/',insert,name='insert'),
    path('view/',view,name='view')
]
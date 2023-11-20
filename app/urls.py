from app.views import *
from django.urls import path
app_name='condition'
urlpatterns=[
    path('ifelse_condition/',ifelse_condition,name='ifelse_condition'),
    path('ifelif_condition/',ifelif_condition,name='ifelif_condition'),
    path('nexted_condition/',nexted_condition,name='nexted_condition'),
]
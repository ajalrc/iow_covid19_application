from . import views
from django.urls import path,include

urlpatterns=[
    path('',views.confirmed_cases, name="confirmed_cases"),
]
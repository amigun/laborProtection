from django.contrib.auth.forms import UsernameField
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views, forms

from .views import *

urlpatterns = [
    path('', WebPassportPage.as_view(), name='WebPassport')
]
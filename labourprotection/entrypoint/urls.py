from django.urls import path, include
from django.views.generic import TemplateView
from entrypoint import views

from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('ep/account/', views.account, name='account'),
    path('', include('django.contrib.auth.urls'))
]
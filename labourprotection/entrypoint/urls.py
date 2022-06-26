from django.urls import path, include
from django.views.generic import TemplateView
from entrypoint.views import account

from .views import *

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('account/', account, name='account'),
    path('', include('django.contrib.auth.urls'))
]
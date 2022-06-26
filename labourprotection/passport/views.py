from django.shortcuts import render
from django.views.generic import CreateView

from .models import *
from .forms import *

# Create your views here.
class WebPassportPage(CreateView):
    form_class = WebPassport
    template_name = 'passport/passport.html'

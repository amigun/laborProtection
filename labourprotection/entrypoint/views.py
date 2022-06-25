from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import TemplateView, View
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login


class index(TemplateView):
    template_name = "entrypoint/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страничка'

        return context


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

        context = {
            'form': form
        }

        return render(request, self.template_name, context)


# def login(request):
#     context = {
#         'title': 'Вход в аккаунт'
#     }
#
#     return render(request, 'entrypoint/login.html', context=context)
#
#
# def registration(request):
#     context = {
#         'title': 'Регистрация нового пользователя'
#     }
#
#     return render(request, 'entrypoint/register.html', context=context)
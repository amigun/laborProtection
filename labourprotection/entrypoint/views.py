from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login
from entrypoint.forms import UserCreationForm


class index(TemplateView):
    template_name = "entrypoint/index.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страничка'

        return context


def account(request):
    template_name = 'entrypoint/account.html'
    if request.user.is_authenticated():
        return render(request, template_name)
    return redirect('https://example.com/')


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
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
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
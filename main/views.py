from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from scores.utils import *
from .forms import *
from django.views.generic import CreateView, FormView


def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(f"Обратная связь: {form.cleaned_data}")
        return redirect('home')




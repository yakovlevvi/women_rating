from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import TyanForm
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .utils import *


class ScoresHome(LoginRequiredMixin, DataMixin, ListView):
    model = Tyans
    template_name = 'scores/scores_home.html'
    context_object_name = 'members'
    login_url = reverse_lazy('scores_home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['current_user'] = current_user
        c_def = self.get_user_context()
        context.update(c_def)
        return context

    def get_queryset(self):
        current_user = self.request.user

        if current_user.is_authenticated:
            members = Tyans.objects.filter(user=current_user).select_related('cat')
            return sorted(members, key=lambda x: x.rating, reverse=True)
        else:
            return []


class ShowPost(DataMixin, DetailView):
    model = Tyans
    template_name = 'scores/post.html'
    slug_url_kwarg = 'post_slug'  # переменная для слага
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ScoresCategory(DataMixin, ListView):
    model = Tyans
    template_name = 'scores/scores_home.html'
    context_object_name = 'members'
    allow_empty = False

    def get_queryset(self):
        return Tyans.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['current_user'] = current_user
        c_def = self.get_user_context(cat_selected=context['members'][0].cat_id)
        context.update(c_def)
        return context


class ScoresUpdateView(UpdateView):
    model = Tyans
    template_name = 'scores/member_form.html'
    form_class = TyanForm


class ScoresDeleteView(DeleteView):
    model = Tyans
    success_url = '/scores/'
    template_name = 'scores/scores-delete.html'


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    model = Tyans
    form_class = TyanForm
    template_name = 'scores/member_form.html'
    success_url = reverse_lazy('scores_home')
    login_url = reverse_lazy('scores_home')
    raise_exception = True

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            return redirect('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))



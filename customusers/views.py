from django.shortcuts import render
from django.views.generic import DetailView, ListView

from scores.models import *
from scores.utils import *


def user_list(request):
    users = TopUser.objects.all()
    return render(request, 'scores/user_list.html', {'users': users})


class ShowUser(DataMixin, DetailView):
    model = TopUser
    template_name = 'scores/user_top.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'  # переменная для слага
    context_object_name = 'user'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class UserScores(DataMixin, ListView):
    model = Article
    template_name = 'scores/user_scores.html'
    context_object_name = 'articles'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.kwargs['username']
        context['current_user'] = current_user
        c_def = self.get_user_context()
        context.update(c_def)
        return context

    def get_queryset(self):
        current_user = self.kwargs['username']
        members = Article.objects.filter(user__username=current_user).select_related('cat')
        return sorted(members, key=lambda x: x.rating, reverse=True)
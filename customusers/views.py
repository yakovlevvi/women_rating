from django.db.models import Avg, F, OuterRef, ExpressionWrapper, FloatField, Subquery, DecimalField
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
    model = TopUser
    template_name = 'customusers/user_ratings_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Подзапрос для усредненных оценок
        avg_ratings = ArticleRating.objects.filter(
            user=OuterRef('pk')  # Связываем с пользователями через их primary key (pk)
        ).annotate(
            avg_rating=ExpressionWrapper(
                (Avg(F('face')) + Avg(F('figure')) + Avg(F('tits')) + Avg(F('ass'))) / 4,
                output_field=FloatField()
            )
        ).values('avg_rating')

        queryset = queryset.annotate(
            avg_rating=Subquery(avg_ratings)
        )

        return queryset


class UserProfileView(DataMixin, DetailView):
    model = TopUser
    template_name = 'customusers/user_profile.html'
    context_object_name = 'user'
    slug_url_kwarg = 'username'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.kwargs['username']  # Получите имя пользователя из URL

        # Вычисляем усредненные рейтинги для статей пользователя с именем username
        user_ratings = ArticleRating.objects.filter(user__username=username)
        average_ratings = {}
        for rating in user_ratings:
            avg_rating = (rating.face + rating.figure + rating.tits + rating.ass) / 4
            average_ratings[rating.article] = avg_rating

        sorted_average_ratings = dict(sorted(average_ratings.items(), key=lambda item: item[1], reverse=True))
        context['average_ratings'] = sorted_average_ratings
        c_def = self.get_user_context()
        context.update(c_def)
        return context

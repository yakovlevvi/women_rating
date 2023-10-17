from django.db.models import ExpressionWrapper, F, DecimalField
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .utils import *


# class ScoresHome(LoginRequiredMixin, DataMixin, ListView):
#     model = Tyans
#     template_name = 'scores/scores_home.html'
#     context_object_name = 'members'
#     login_url = reverse_lazy('scores_home')
#     raise_exception = True
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         current_user = self.request.user
#         context['current_user'] = current_user
#         c_def = self.get_user_context()
#         context.update(c_def)
#         return context
#
#     def get_queryset(self):
#         current_user = self.request.user
#
#         if current_user.is_authenticated:
#             members = Tyans.objects.filter(user=current_user).select_related('cat')
#             return sorted(members, key=lambda x: x.rating, reverse=True)
#         else:
#             return []


class ArticleList(DataMixin, ListView):
    model = Article
    template_name = 'scores/article_list.html'
    context_object_name = 'articles'
    ordering = ['-total_rating']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        c_def = self.get_user_context()
        context.update(c_def)
        return context

    # def get_queryset(self):
    #     current_user = self.request.user
    #
    #     if current_user.is_authenticated:
    #         articles = Article.objects.all().select_related('cat')
    #         return articles
    #     else:
    #         return []


class ShowPost(DataMixin, DetailView):
    model = Article
    template_name = 'scores/post.html'
    slug_url_kwarg = 'post_slug'  # переменная для слага
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


class ScoresCategory(DataMixin, ListView):
    model = Article
    template_name = 'scores/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = context.get('articles', None)
        if articles:
            c_def = self.get_user_context(cat_selected=context['articles'][0].cat_id)
            context.update(c_def)
        return context


class ScoresUpdateView(UpdateView):
    model = ArticleRating
    template_name = 'scores/rate_article.html'
    form_class = ArticleRatingForm

    def get_object(self, queryset=None):
        # Получите оценку (ArticleRating) на основе slug статьи и пользователя
        slug = self.kwargs['article_slug']
        user = self.request.user
        return ArticleRating.objects.get(article__slug=slug, user=user)

    def form_valid(self, form):
        article = form.instance.article
        article_rating = form.instance
        article_rating.user = self.request.user
        article_rating.save()

        total_ratings = ArticleRating.objects.filter(article=article)
        total_rating_sum = sum(
            (rating.face + rating.figure + rating.tits + rating.ass) / 4 for rating in total_ratings
        )
        article.total_rating = total_rating_sum / total_ratings.count()
        article.user_count = total_ratings.count()
        article.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = self.object.article
        return context

    def get_success_url(self):
        # Здесь вы можете указать URL-адрес, куда перенаправить пользователя
        # Например, перенаправить обратно на страницу статьи
        return reverse('article_list')


class ScoresDeleteView(DeleteView):
    model = Article
    success_url = '/scores/'
    template_name = 'scores/scores-delete.html'


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    model = Article
    form_class = TyanForm
    template_name = 'scores/member_form.html'
    success_url = reverse_lazy('article_list')
    login_url = reverse_lazy('article_list')
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


def rate_article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)

    if request.method == 'POST':
        rating_form = ArticleRatingForm(request.POST)
        if rating_form.is_valid() and request.user.is_authenticated:
            if not ArticleRating.objects.filter(user=request.user, article=article).exists():
                article_rating = rating_form.save(commit=False)
                article_rating.user = request.user
                article_rating.article = article
                article_rating.save()

                total_ratings = ArticleRating.objects.filter(article=article)
                total_rating_sum = sum(
                    (rating.face + rating.figure + rating.tits + rating.ass) / 4 for rating in total_ratings
                )
                article.total_rating = total_rating_sum / total_ratings.count()
                article.user_count = total_ratings.count()
                article.save()
            return redirect('article_list')
        else:
            return redirect('article_list')

    rating_form = ArticleRatingForm()
    return render(request, 'scores/rate_article.html', {'article': article, 'form': rating_form})


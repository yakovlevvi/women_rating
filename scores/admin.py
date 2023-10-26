from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_html_photo', 'created_at', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'created_at')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'cat', 'age', 'total_rating', 'user_count', 'photo', 'is_published')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo}' width=50>")

    get_html_photo.short_description = "Фото"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(TopUser)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleRating)


admin.site.site_title = 'Админ-панель сайта чарта индейца'
admin.site.site_header = 'Админ-панель сайта чарта индейца'

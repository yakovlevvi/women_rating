from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class TyanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'get_html_photo', 'date', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'date')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'date')
    prepopulated_fields = {'slug': ('name',)}
    fields = ('name', 'slug', 'user', 'cat', 'age', 'face', 'figure', 'tits', 'ass', 'image', 'get_html_photo', 'is_published')
    readonly_fields = ('date', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image}' width=50>")

    get_html_photo.short_description = "Фото"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Tyans, TyanAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(TopUser)
admin.site.register(Article)
admin.site.register(ArticleRating)

admin.site.site_title = 'Админ-панель сайта чарта индейца'
admin.site.site_header = 'Админ-панель сайта чарта индейца'

from django.contrib import admin
from .models import Article, Tag, Scope


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)

from django.contrib import admin

from articles.models import Article, Reporter

admin.site.register(Article)
admin.site.register(Reporter)

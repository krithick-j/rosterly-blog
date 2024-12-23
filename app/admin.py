from django.contrib import admin

from app.models.article import Article
from app.models.color import Color

# Register your models here.
admin.site.register(Color)
admin.site.register(Article)
from app.controllers.article import article
from django.urls import path

urlpatterns = [
    path('article/', article),
]

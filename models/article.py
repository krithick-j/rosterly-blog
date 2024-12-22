from django.db import models
from models.user import CustomUser

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.JSONField(default=list)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
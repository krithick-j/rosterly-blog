from django.db import models
from app.models.color import Color

class Article(models.Model):
    color = models.ForeignKey(Color, null=True, blank=True, on_delete=models.CASCADE, related_name='color')
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.JSONField(default=list)
    # author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

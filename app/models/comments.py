from django.db import models

from app.models.article import Article
from app.models.user import User

class Comment(models.Model):
    content = models.TextField()  # The text content of the comment.
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name='comments'  # Links the comment to its article.
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments'  # Links the comment to its author.
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the comment is created.

from rest_framework import serializers
from app.models.article import Article
from app.serializers.color import ColorSerializer

class ArticleSerializer(serializers.ModelSerializer):
    color = ColorSerializer()
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'color', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']

    def validate(self, data):
        special_char = '!@#$%^&*()-_=+{[|\:;">.<,?/]}'
        if any(c in special_char for c in data['title']):
            raise serializers.ValidationError("Title cannot have special characters")
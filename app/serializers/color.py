from rest_framework import serializers

from app.models.color import Color

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name']
        # read_only_fields = ['author', 'created_at', 'updated_at']
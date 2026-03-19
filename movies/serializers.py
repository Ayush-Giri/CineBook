from rest_framework.serializers import ModelSerializer
from movies.models import Movies
from rest_framework import serializers



class MovieSerializer(ModelSerializer):
    language_type = serializers.CharField(source="language.language", read_only=True)
    genre_type = serializers.CharField(source="genre.genre", read_only=True)

    class Meta:
        model = Movies
        fields = [
            "id",
            "title",
            "description",
            "duration_in_minutes",
            "release_date",
            "genre",
            "genre_type",
            "language",
            "language_type",
            "poster_image",
            "is_active",
            "created_at",
        ]
        read_only_fields = ['created_at']

    
    def validate_duration_in_minutes(self, value):
        if value <= 0:
            raise serializers.ValidationError("minutes cannot be 0 or less")
        return value
from rest_framework.serializers import ModelSerializer
from movies.models import Movies
from rest_framework import serializers
import datetime 



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


    def to_internal_value(self, data):
        """
        modifying our data as this is what will get converted to python object before saving it to the database
        """
        movie_title = data.get('title').strip()
        data['title'] = movie_title
        return super().to_internal_value(data) # and again now change it python object then send it



    
    def validate_duration_in_minutes(self, value):
        if value <= 0:
            raise serializers.ValidationError("minutes cannot be 0 or less")
        return value
    

    def to_representation(self, instance):
        """
        controls how the data is sent to front end we can modify it as per will
        """
        data = super().to_representation(instance) # convert the python object to dict
        total_minutes = data["duration_in_minutes"]
        hours = total_minutes // 60
        minutes = total_minutes - (hours * 60)

        data.pop("duration_in_minutes")

        data["duration"] = f"{hours}h {minutes}m"

        if data["poster_image"] is None:
            data.pop("poster_image")
        current_date = datetime.date.today()
        if instance.release_date > current_date:
            data["is_upcoming"] = True
        return data # now send the modified dict to front end
from rest_framework import serializers
from shows.models import Shows
from theatres.models import Screen
from movies.serializers import MovieSerializer



class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    screen_detail = ScreenSerializer(source="screen", read_only=True)
    movie_detail = MovieSerializer(source="movie", read_only=True)
    class Meta:
        model = Shows
        fields = [
            "id",
            "movie",
            "movie_detail",
            "screen",
            "screen_detail",
            "start_time",
            "end_time",
            "is_active",
        ]

# Answer these:
# Question 1:
# How do you structure BookingSerializer to satisfy both requirements? Explain the fields you'd add and why.
# Question 2:
# Your show_detail nested serializer is returning the full Show object including screen as just an ID. Frontend now wants screen to also be nested inside show_detail. What do you change and where?
# Question 3:
# A junior dev on your team says "just remove read_only=True from the nested serializer so it works for both reads and writes." What's wrong with this suggestion?
# No code needed — explain in plain English. 🎯
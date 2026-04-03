from rest_framework import serializers
from shows.models import Shows
from theatres.models import Screen
from movies.serializers import MovieSerializer
from bookings.models import Booking
from theatres.models import Screen



class ScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screen
        fields = "__all__"


class ShowSerializer(serializers.ModelSerializer):
    screen_detail = ScreenSerializer(source="screen", read_only=True)
    movie_detail = MovieSerializer(source="movie", read_only=True)
    available_seats = serializers.SerializerMethodField()
    house_full_status = serializers.SerializerMethodField()
    formatted_duration = serializers.SerializerMethodField()
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
            "available_seats",
            "house_full_status",
            "formatted_duration",
        ]

    def get_available_seats(self, obj):
        return obj.screen.total_seats
    
    
    def get_house_full_status(self, obj):
        return False
    
    def get_formatted_duration(self, obj):
        total_minutes = obj.movie.duration_in_minutes
        hour = total_minutes // 60
        minutes = (total_minutes) -  hour * 60
        return f"{hour}h {minutes}m"
    



# Answer these:
# Question 1:
# How do you structure BookingSerializer to satisfy both requirements? Explain the fields you'd add and why.
# Question 2:
# Your show_detail nested serializer is returning the full Show object including screen as just an ID. Frontend now wants screen to also be nested inside show_detail. What do you change and where?
# Question 3:
# A junior dev on your team says "just remove read_only=True from the nested serializer so it works for both reads and writes." What's wrong with this suggestion?
# No code needed — explain in plain English. 🎯
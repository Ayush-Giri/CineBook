from rest_framework import serializers
from bookings.models import Booking, BookedSeat
from shows.models import Shows


class ShowDetailSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    class Meta:
        model = Shows
        fields = [
            "movie",
            "movie_title",
        ]



class BookingSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    show_detail = ShowDetailSerializer(source="show", read_only=True)
    status_detail = serializers.CharField(source="status.status", read_only=True)

    class Meta:
        model = Booking
        fields = [
            'user',
            'username',
            'show',
            "show_detail",
            'status',
            'total_price',
            'created_at',
        ]

    
    def validate_total_price(self, value):
        """
        use validate_field name to validate a field
        """
        if value <= 0:
            raise serializers.ValidationError("Price cannot be 0 or less")
        return value
    
    
    def validate_show(self, value):
        if value.is_active != True:
            raise serializers.ValidationError("cannot book inactive show")
        return value
    

    
    def validate(self, data):
        """
        data if front end json which has gone through field validation and is now
        a dictinary which is passed automatically

        use validate method when validation depends on some kind of logic
        like here the same user cannot book for the same show more than 3 times
        """
        if Booking.objects.filter(user=data['user'], show=data['show']).count() >= 3:
            raise serializers.ValidationError("single users cannot make more than 3 bookings")





class BookedSeatSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookedSeat
        fields = [
            "booking",
            "seat"
        ]
        depth=2


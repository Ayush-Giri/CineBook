from rest_framework import serializers
from bookings.models import Booking, BookedSeat
from shows.models import Shows
from django.contrib.auth import get_user_model


User = get_user_model()

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ShowDetailSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source="movie.title", read_only=True)
    class Meta:
        model = Shows
        fields = [
            "movie",
            "movie_title",
        ]



class BookingSerializer(serializers.ModelSerializer):
    """
    as soon as data passes through serializer the foreign key fields are automatically resloved to instances
    """
    # username = serializers.CharField(source='user.username', read_only=True)
    user_detail = UserDetailSerializer(source="user", read_only=True)
    show_detail = ShowDetailSerializer(source="show", read_only=True)
    status_detail = serializers.CharField(source="status.status", read_only=True)

    class Meta:
        model = Booking
        fields = [
            'user',
            'user_detail',
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
        
    def to_representation(self, instance):
        data =  super().to_representation(instance)
        data["total_price"] = f"NPR: {data['total_price']}"

        if instance.status.status == "pending":
            data["is_cancellable"] = True
        else:
            data["is_cancellable"] = False

        """
        context is passed into serializer we have seen that so many times and there we pass the rquest object we
        can see for the suer
        """

        request_object = self.context.get("request") # there maybe case where no context is passed
        if request_object:
            if not request_object.user.is_staff:
                data.pop("created_at", None)

        return data





class BookedSeatSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookedSeat
        fields = [
            "booking",
            "seat"
        ]
        depth=2


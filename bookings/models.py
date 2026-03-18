from django.db import models
from django.contrib.auth import get_user_model
from shows.models import Shows
from theatres.models import Seat

# Create your models here.


User = get_user_model()

class Status(models.Model):
    class Meta:
        verbose_name = "status"
        verbose_name_plural = "statuses"

    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.status}"
    


class Booking(models.Model):
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Shows, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        f"{self.user.username} | {self.status.status} | {self.total_price} | {self.created_at}"




class BookedSeat(models.Model):
    class Meta:
        verbose_name = "Booked Seat"
        verbose_name_plural = "Booked Seats"
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)



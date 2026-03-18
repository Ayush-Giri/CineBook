from django.db import models
from bookings.models import Booking
from .helpers import generate_txn_id

# Create your models here.




class BookingStatus(models.Model):
    class Meta:
        verbose_name = "Booking Status"
        verbose_name_plural = "Booking Statues"
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.status}"
    

class Booking(models.Model):
    class Meta:
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    booking_status = models.ForeignKey(BookingStatus, on_delete=models.CASCADE)
    transaction_id = models.CharField(
        max_length=10,
        unique=True,
        default=generate_txn_id,
        editable=False
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.booking} | {self.amount} | {self.booking_status.status} | {self.transaction_id}"






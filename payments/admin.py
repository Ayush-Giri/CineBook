from django.contrib import admin
from payments.models import BookingStatus, Booking

# Register your models here.

admin.site.register(BookingStatus)
admin.site.register(Booking)


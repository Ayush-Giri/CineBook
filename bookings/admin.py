from django.contrib import admin
from bookings.models import Status, BookedSeat, Booking

# Register your models here.

admin.site.register(Status)
admin.site.register(BookedSeat)
admin.site.register(Booking)


# start from payments app

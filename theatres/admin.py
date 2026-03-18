from django.contrib import admin
from theatres.models import City, Theatre, Screen, Row, SeatType, Seat

# Register your models here.
admin.site.register(City)
admin.site.register(Theatre)
admin.site.register(Screen)
admin.site.register(Row)
admin.site.register(SeatType)
admin.site.register(Seat)
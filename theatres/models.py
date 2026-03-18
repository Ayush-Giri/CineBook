from django.db import models

# Create your models here.


class City(models.Model):
    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Theatre(models.Model):
    class Meta:
        verbose_name = "Theatre"
        verbose_name_plural = "Theatres"
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    total_screens = models.IntegerField()


    def __str__(self):
        return f"{self.name} | {self.city}"



class Screen(models.Model):
    class Meta:
        verbose_name = "Screen"
        verbose_name_plural = "Screens"
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen_number = models.IntegerField()
    total_seats = models.IntegerField()


    def __str__(self):
        return f"{self.theatre.name} | {self.screen_number} | {self.total_seats}"
    


class Row(models.Model):
    class Meta:
        verbose_name = "Row"
        verbose_name_plural = "Rows"
    row = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.row}"
    


class SeatType(models.Model):
    class Meta:
        verbose_name = "seat type"
        verbose_name_plural = "Seat Types"
    seat_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.seat_type}"
    

class Seat(models.Model):
    class Meta:
        verbose_name = "Seat"
        verbose_name_plural = "Seats"
    row = models.ForeignKey(Row, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    seat_type = models.ForeignKey(SeatType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.row.row} | {self.seat_number} | {self.seat_type} | {self.price} "


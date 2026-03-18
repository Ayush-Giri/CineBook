from django.db import models
from movies.models import Movies
from theatres.models import Screen

# Create your models here.

class Shows(models.Model):
    class Meta:
        verbose_name = "Show"
        verbose_name_plural = "Shows"
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.movie.title} | {self.start_time} | {self.end_time} | {self.is_active}"


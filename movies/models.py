from django.db import models

# Create your models here.


class Genre(models.Model):
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    genre = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.genre}"
    



class Language(models.Model):
    class Meta:
        verbose_name = "Langauge"
        verbose_name_plural = "Languagedds"
    language = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.language}"
    



class Movies(models.Model):
    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration_in_minutes = models.IntegerField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    poster_image = models.ImageField(upload_to="posters", null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} | {self.description} | {self.release_date} | {self.language}"

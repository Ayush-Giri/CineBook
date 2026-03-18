from django.db import models
from django.contrib.auth import get_user_model
from movies.models import Movies

# Create your models here.

User = get_user_model()

class Review(models.Model):
    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
        unique_together = ["user", "movie"]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        f"{self.user.username} | {self.movie.title} | \
            {self.rating} | {self.comment} | {self.created_at}"
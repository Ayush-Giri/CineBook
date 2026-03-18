from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class Notification(models.Model):
    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} | {self.title} | \
            {self.message} | {self.is_read} | {self.created_at}"

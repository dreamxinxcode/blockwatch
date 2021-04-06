from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        def __str__(self):
            return self.title

from django.db import models
from autoslug import AutoSlugField


class Province(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        def __str__(self):
            return self.title


class City(models.Model):
    title = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='title')

    class Meta:
        def __str__(self):
            return self.title

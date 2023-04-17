from django.core.files.base import ContentFile
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    cover_type = models.CharField(max_length=50)
    dimensions = models.CharField(max_length=50)
    pub_date = models.DateField()
    poster = models.ImageField(upload_to='image/', null=True)

    def save(self, *args, **kwargs):
        if self.poster:
            if isinstance(self.poster, memoryview):
                self.poster = ContentFile(self.poster)
            super().save(*args, **kwargs)
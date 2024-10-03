from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rate = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)])
    location = models.TextField(default='Tashkent', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hotel'
        verbose_name_plural = 'Hotels'
        ordering = ['-created']


class PictureModel(models.Model):
    image = models.ImageField(upload_to='hotels/')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel.name

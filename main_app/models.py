from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Influncer(models.Model):
    name = models.CharField(max_length=50)
    real_name = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=250, blank=True)
    image_url = models.CharField(max_length=250, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'toy_id': self.id})

class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, default='BTC', blank=True)
    description = models.TextField(max_length=400, blank=True)
    price = models.FloatField(default=0.00)
    website = models.CharField(max_length=250, blank=True)
    api_name = models.CharField(max_length=250, blank=True)
    image_url = models.CharField(max_length=250, blank=True)
    influncer = models.ManyToManyField(Influncer, blank=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('toys_d1etail', kwargs={'toy_id': self.id})
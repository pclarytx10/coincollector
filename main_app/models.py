from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Influencer(models.Model):
    name = models.CharField(max_length=50)
    real_name = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=250, blank=True)
    image_url = models.CharField(max_length=250, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('influencers_detail', kwargs={'influencer_id': self.id})

class Coin(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10, default='BTC', blank=True)
    description = models.TextField(max_length=600, blank=True)
    price = models.FloatField(default=0.00)
    website = models.CharField(max_length=250, blank=True)
    api_name = models.CharField(max_length=250, blank=True)
    image_url = models.CharField(max_length=250, blank=True)
    influencer = models.ManyToManyField(Influencer, blank=True)
    
    class Meta:
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('coins_detail', kwargs={'coin_id': self.id})
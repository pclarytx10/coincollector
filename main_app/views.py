from django.shortcuts import render, redirect
from .models import Coin, Influncer


# Create your views here.
# Define the home view
def home(request):
  return render(request, 'home.html')

# Define the about view
def about(request):
  return render(request, 'about.html')

# Define the coins index view
def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'coins/index.html', { 'coins': coins })

# Define the influencers index view
def influencers_index(request):
    influencers = Influncer.objects.all()
    return render(request, 'influencers/index.html', { 'influencers': influencers })
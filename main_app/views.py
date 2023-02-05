from django.shortcuts import render, redirect
from .models import Coin, Influencer


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

# Define the coins detail view
def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    return render(request, 'coins/detail.html', { 'coin': coin })

# Define the influencers index view
def influencers_index(request):
    influencers = Influencer.objects.all()
    return render(request, 'influencers/index.html', { 'influencers': influencers })

#Define the influencers detail view
def influencers_detail(request, influencer_id):
    influencer = Influencer.objects.get(id=influencer_id)
    return render(request, 'influencers/detail.html', { 'influencer': influencer })

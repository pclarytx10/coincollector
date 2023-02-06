from django.shortcuts import render, redirect
from .models import Coin, Influencer
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Import login_required to protect def views
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin

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

def signup(request):
  error_message = ''
  # If the request method is POST, this is a sign-up attempt
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

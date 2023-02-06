from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.coins_index, name='index'),
    path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
    path('influencers/', views.influencers_index, name='inf_index'),
    path('influencers/<int:influencer_id>/', views.influencers_detail, name='inf_detail'),
    path('accounts/signup/', views.signup, name='signup'),  
]
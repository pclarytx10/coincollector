from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.coins_index, name='index'),
    path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
    path('coins/create/', views.CoinCreate.as_view(), name='coins_create'),
    path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
    path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
    path('influencers/', views.influencers_index, name='inf_index'),
    path('influencers/<int:influencer_id>/', views.influencers_detail, name='inf_detail'),
    path('influencers/create/', views.InfluencerCreate.as_view(), name='influencers_create'),
    path('influencers/<int:pk>/update/', views.InfluencerUpdate.as_view(), name='influencers_update'),
    path('influencers/<int:pk>/delete/', views.InfluencerDelete.as_view(), name='influencers_delete'),
    path('accounts/signup/', views.signup, name='signup'),  
]
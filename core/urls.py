from django.urls import path ,include
from .views import *
#from .views import posts ,postsDetail
urlpatterns = [
    path('coinsentiment/<int:id>', CoinSentimentList.as_view()),
    path('updatesentiment/<int:id>', UpdateCoin.as_view()),
]
from django.http import HttpResponse
from .models import *
from .serializers import *
import math, random
from datetime import datetime
import datetime as dt
import tweepy
import preprocessor as p
import re
#nltk.data.path.append('./nltk_data/')
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
class Tweet(object):

    def __init__(self, content, polarity):
        self.content = content
        self.polarity = polarity
from textblob import TextBlob
consumer_key= '4mLWXS9vve7E30sQToMCvBcD3'
consumer_secret= 'v4EiJIwapQDUv46hpquGHBiEVnOMnHLcXq2QHLCfQNeqPwJr17'

access_token='1454745623798812676-I3fG3xIYX27vBavuo58RhxTVhX1to8'
access_token_secret='gHfX5uAyOWszMfxD181CWo2ZLElowKzWJfnPaxq4wAoBE'

num_of_tweets = int(300)
def retrieving_tweets_polarity(symbol):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    user = tweepy.API(auth)
    tweets = tweepy.Cursor(user.search, q=symbol,tweet_mode='extended', lang='en',exclude_replies=True).items(num_of_tweets)    
    tweet_list = [] #List of tweets alongside polarity
    global_polarity = 0 #Polarity of all tweets === Sum of polarities of individual tweets
    tw_list=[] #List of tweets only => to be displayed on web page
    #Count Positive, Negative to plot pie chart
    pos=0 #Num of pos tweets
    neg=1 #Num of negative tweets
    for tweet in tweets:
        count=20 #Num of tweets to be displayed on web page
        #Convert to Textblob format for assigning polarity
        tw2 = tweet.full_text
        tw = tweet.full_text
        #Clean
        tw=p.clean(tw)
        #print("-------------------------------CLEANED TWEET-----------------------------")
        #print(tw)
        #Replace &amp; by &
        tw=re.sub('&amp;','&',tw)
        #Remove :
        tw=re.sub(':','',tw)
        #print("-------------------------------TWEET AFTER REGEX MATCHING-----------------------------")
        #print(tw)
        #Remove Emojis and Hindi Characters
        tw=tw.encode('ascii', 'ignore').decode('ascii')
        #print("-------------------------------TWEET AFTER REMOVING NON ASCII CHARS-----------------------------")
        #print(tw)
        blob = TextBlob(tw)
        polarity = 0 #Polarity of single individual tweet
        for sentence in blob.sentences:           
            polarity += sentence.sentiment.polarity
            if polarity>0:
                pos=pos+1
            if polarity<0:
                neg=neg+1
            
            global_polarity += sentence.sentiment.polarity
        if count > 0:
            tw_list.append(tw2)
            
        tweet_list.append(Tweet(tw, polarity))
        count=count-1
    if len(tweet_list) != 0:
        global_polarity = global_polarity / len(tweet_list)
    else:
        global_polarity = global_polarity
    neutral=num_of_tweets-pos-neg
    if neutral<0:
        neg=neg+neutral
        neutral=20
    return global_polarity,pos,neg,neutral


class CoinSentimentList(APIView):
    def get(self,request,id):
        if(id==0):
            try :
                data  = BitcoinSentiment.objects.all()
                serializer = BitcoinSerializer(data , many=True)
            except BitcoinSentiment.DoesNotExist :
                serializer = BitcoinSerializer(many=True)
        if(id==1):
            try :
                data  = EthereumSentiment.objects.all()
                serializer = EthereumSerializer(data,many=True)
            except EthereumSentiment.DoesNotExist :
                serializer = EthereumSerializer(many=True)
        if(id==2):
            try :
                data  = BinanceCoinSentiment.objects.all()
                serializer = BinanceCoinSerializer(data ,many=True)
            except BinanceCoinSentiment.DoesNotExist :
                serializer = BinanceCoinSerializer(many=True)
        if(id==3):
            try :
                data  = CardanoSentiment.objects.all()
                serializer = CardanoSerializer(data ,many=True)
            except CardanoSentiment.DoesNotExist :
                serializer = CardanoSerializer(many=True)
        if(id==4):
            try :                
                data  = SolanaSentiment.objects.all()
                serializer = SolanaSerializer(data ,many=True)
            except SolanaSentiment.DoesNotExist :
                serializer = SolanaSerializer(many=True)
        if(id==5):
            try :
                data  = PolkadotSentiment.objects.all()
                serializer = PolkadotSerializer(data,many=True)
            except PolkadotSentiment.DoesNotExist :
                serializer = PolkadotSerializer(many=True)
        if(id==6):
            try :
                data  = ShibaInuSentiment.objects.all()
                serializer = ShibaInuSerializer(data,many=True)
            except ShibaInuSentiment.DoesNotExist :
                serializer = ShibaInuSerializer(many=True)
        if(id==7):
            try :
                data  = DogeCoinSentiment.objects.all()
                serializer = DogeCoinSerializer(data,many=True)
            except DogeCoinSentiment.DoesNotExist :
                serializer = DogeCoinSerializer(many=True)
        if(id==8):
            try :
                data  = TerraSentiment.objects.all()
                serializer = TerraSerializer(data,many=True)
            except TerraSentiment.DoesNotExist :
                serializer = TerraSerializer(many=True)
        if(id==9):
            try :
                data  = LitecoinSentiment.objects.all()
                serializer = LitecoinSerializer(data,many=True)
            except LitecoinSentiment.DoesNotExist :
                serializer = LitecoinSerializer(many=True)
        return Response(serializer.data)        
def updateCryptoSentiment(no):
    coin = ["bitcoin","ethereum","binance coin","cardano","solana","polkadot","shiba inu","dogecoin","terra","litecoin"]
    j=no
    for i in range(0,2) :
        t=j+i
        symbol = coin[t]
        a = retrieving_tweets_polarity(symbol)
        now = datetime.now()
        if(t==0):
            try :
                b = BitcoinSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except BitcoinSentiment.DoesNotExist :
                b = BitcoinSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==1):
            try :
                b = EthereumSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except EthereumSentiment.DoesNotExist :
                b = EthereumSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==2):
            try :
                b = BinanceCoinSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except BinanceCoinSentiment.DoesNotExist :
                b = BinanceCoinSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==3):
            try :
                b = CardanoSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except CardanoSentiment.DoesNotExist :
                b = CardanoSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==4):
            try :
                b = SolanaSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except SolanaSentiment.DoesNotExist :
                b = SolanaSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==5):
            try :
                b = PolkadotSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except PolkadotSentiment.DoesNotExist :
                b = PolkadotSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==6):
            try :
                b = ShibaInuSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except ShibaInuSentiment.DoesNotExist :
                b = ShibaInuSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==7):
            try :
                b = DogeCoinSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except DogeCoinSentiment.DoesNotExist :
                b = DogeCoinSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==8):
            try :
                b = TerraSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except TerraSentiment.DoesNotExist :
                b = TerraSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
        if(t==9):
            try :
                b = LitecoinSentiment.objects.get(Date=now)
                b.Date = now
                b.save()
            except LitecoinSentiment.DoesNotExist :
                b = LitecoinSentiment(FearIndex=a[0], Positive=a[1], Negative = a[2], Neutral = a[3])
                b.save()
class UpdateCoin(APIView):
    def get(self,request,id):
        updateCryptoSentiment(id)
        return Response(status=status.HTTP_200_OK)
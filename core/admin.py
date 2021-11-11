from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(BitcoinSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(EthereumSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(BinanceCoinSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(CardanoSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(SolanaSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(PolkadotSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(ShibaInuSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(DogeCoinSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(TerraSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]
@admin.register(LitecoinSentiment)
class dataModel(admin.ModelAdmin):
    list_display=["Date","FearIndex","Positive","Negative","Neutral"]

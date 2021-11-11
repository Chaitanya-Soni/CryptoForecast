from rest_framework import serializers
from .models import *
class BitcoinSerializer(serializers.ModelSerializer):
    class Meta :
        model = BitcoinSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class EthereumSerializer(serializers.ModelSerializer):
    class Meta :
        model = EthereumSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class BinanceCoinSerializer(serializers.ModelSerializer):
    class Meta :
        model = BinanceCoinSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class CardanoSerializer(serializers.ModelSerializer):
    class Meta :
        model = CardanoSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class SolanaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolanaSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class PolkadotSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolkadotSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class ShibaInuSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShibaInuSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class DogeCoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = DogeCoinSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class TerraSerializer(serializers.ModelSerializer):
    class Meta:
        model = TerraSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
class LitecoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = LitecoinSentiment
        fields = ["id","Date","FearIndex","Positive","Negative","Neutral"]
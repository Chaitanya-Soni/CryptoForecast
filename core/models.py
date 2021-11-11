from django.db import models
# Create your models here.
#1
class BitcoinSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=True)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#2
class EthereumSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=True)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#3
class BinanceCoinSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=True)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#4
class CardanoSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=True)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#5
class SolanaSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#6
class PolkadotSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#7
class ShibaInuSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#8
class DogeCoinSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
#9
class TerraSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'

class LitecoinSentiment(models.Model):
    Date = models.DateField(auto_now=False, auto_now_add=False)
    FearIndex = models.FloatField()
    Positive = models.IntegerField()
    Negative = models.IntegerField()
    Neutral = models.IntegerField()
    def __str__(self):
        return str(self.Date)
    class Meta:
        order_with_respect_to = 'Date'
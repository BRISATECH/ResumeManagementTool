from django.db import models

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
class Choice(models.Model): 
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
    
# class Car(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=5, decimal_places=2)
#     photo = models.ImageField(upload_to='cars')

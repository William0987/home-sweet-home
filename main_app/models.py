from django.db import models

class Home(models.Model):
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    square_footage = models.CharField(max_length=200)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    home_type = models.CharField(max_length=200)
    # def __str__(self):
    #     return self.home_text
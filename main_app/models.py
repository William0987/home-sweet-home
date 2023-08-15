from django.db import models

RATINGS = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)

class Furniture(models.Model):
    furniture_type = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=100)
    length = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, default="Enter Description Here...")

    def __str__(self):
        return f'{self.furniture_type} ({self.id})'
    
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'furniture_id': self.id})

class Home(models.Model):
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    square_footage = models.CharField(max_length=200)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    home_type = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="Enter Description Here...")
    furnitures = models.ManyToManyField(Furniture)
    
    def __str__(self):
        return f'{self.address} ({self.id})'
    
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'home_id': self.id})


class Rent(models.Model):
    monthly_price = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    square_footage = models.CharField(max_length=200)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    home_type = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default="Enter Description Here...")
    
    def __str__(self):
        return f'{self.address} ({self.id})'
    
  
    def get_absolute_url(self):
        return reverse('detail', kwargs={'rent_id': self.id})

class Review(models.Model):
    rating = models.IntegerField(
        choices=RATINGS,
    )
    description = models.CharField(
        max_length=1500,
        default="Enter your review here..."
    )

    home = models.ForeignKey(Home, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-rating']

class Tour(models.Model):
    date = models.DateField('tour date')
    time = models.CharField()

    home = models.ForeignKey(Home, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    home = models.ForeignKey(Home, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for home_id: {self.home_id} @{self.url}"
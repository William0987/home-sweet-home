from django.forms import ModelForm
from .models import Review, Tour

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['rating', 'description']

class TourForm(ModelForm):
  class Meta:
    model = Tour
    fields = ['date', 'time']

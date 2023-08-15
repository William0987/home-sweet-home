from django.forms import ModelForm
from .models import Review, Tour, RentReview, RentTour, FurnitureReview

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['rating', 'description']

class TourForm(ModelForm):
  class Meta:
    model = Tour
    fields = ['date', 'time']

class RentReviewForm(ModelForm):
  class Meta:
    model = RentReview
    fields = ['rating', 'description']

class RentTourForm(ModelForm):
  class Meta:
    model = RentTour
    fields = ['date', 'time']

class FurnitureReviewForm(ModelForm):
  class Meta:
    model = FurnitureReview
    fields = ['rating', 'description']

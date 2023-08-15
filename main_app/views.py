import os
import uuid
import boto3
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Home, Rent, Furniture, Review, Tour, Photo, RentReview, RentTour, RentPhoto, FurnitureReview, FurniturePhoto
from .forms import ReviewForm, TourForm, RentReviewForm, RentTourForm, FurnitureReviewForm

def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def homes_index(request):
    homes = Home.objects.all()
    return render(request, 'homes/index.html', 
    { 
        'homes': homes
        }
    )

def homes_detail(request, home_id):
    home = Home.objects.get(id=home_id)
    id_list = home.furnitures.all().values_list('id')
    furnitures_home_doesnt_have = Furniture.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    tour_form = TourForm()
    return render(request, 'homes/detail.html', {
        'home': home,
        'furnitures': furnitures_home_doesnt_have,
        'review_form': review_form,
        'tour_form': tour_form,
        })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class HomeCreate(LoginRequiredMixin, CreateView):
    model = Home
    fields = ['address', 'price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/homes'
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

class HomeUpdate(LoginRequiredMixin, UpdateView):
    model = Home
    fields = ['address', 'price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/homes'
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)
    
class HomeDelete(LoginRequiredMixin, DeleteView):
    model = Home
    success_url = '/homes'
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)
    
def rents_index(request):
    rents = Rent.objects.all()
    return render(request, 'rents/index.html', 
    { 
        'rents': rents
        }
    )

def rents_detail(request, rent_id):
    rent = Rent.objects.get(id=rent_id)
    rent_review_form = RentReviewForm()
    rent_tour_form = RentTourForm()
    return render(request, 'rents/detail.html', {
        'rent': rent,
        'rent_review_form': rent_review_form,
        'rent_tour_form': rent_tour_form
        })

class RentCreate(LoginRequiredMixin, CreateView):
    model = Rent
    fields = ['address', 'monthly_price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/rents'
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)
    
class RentUpdate(LoginRequiredMixin, UpdateView):
    model = Rent
    fields = ['address', 'monthly_price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/rents'
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

class RentDelete(LoginRequiredMixin, DeleteView):
    model = Rent
    success_url = '/rents'
    def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

def furnitures_index(request):
  furnitures = Furniture.objects.all()
  return render(request, 'furnitures/index.html', 
  { 
    'furnitures': furnitures
    }
)

def furnitures_detail(request, furniture_id):
  furniture = Furniture.objects.get(id=furniture_id)
  furniture_review_form = FurnitureReviewForm()
  return render(request, 'furnitures/detail.html', {
    'furniture': furniture,
    'furniture_review_form': furniture_review_form,
  })

class FurnitureCreate(LoginRequiredMixin, CreateView):
  model = Furniture
  fields = '__all__'
  success_url = '/furnitures'
  def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)
  
class FurnitureUpdate(LoginRequiredMixin, UpdateView):
  model = Furniture
  fields = ['furniture_type', 'price', 'color', 'length', 'width', 'height', 'description']
  success_url = '/furnitures'
  def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)

class FurnitureDelete(LoginRequiredMixin, DeleteView):
  model = Furniture
  success_url = '/furnitures'
  def form_valid(self, form):
      form.instance.user = self.request.user 
      return super().form_valid(form)
  
def assoc_furniture(request, home_id, furniture_id):
  Home.objects.get(id=home_id).furnitures.add(furniture_id)
  return redirect('detail', home_id=home_id)

def unassoc_furniture(request, home_id, furniture_id):
  Home.objects.get(id=home_id).furnitures.remove(furniture_id)
  return redirect('detail', home_id=home_id)

@login_required
def add_review(request, home_id):
  form = ReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.home_id = home_id
    new_review.save()
  return redirect('detail', home_id=home_id)

@login_required
def add_tour(request, home_id):
  form = TourForm(request.POST)
  print(form)
  if form.is_valid():
    new_tour = form.save(commit=False)
    new_tour.home_id = home_id
    new_tour.save()
  return redirect('detail', home_id=home_id)

@login_required
def add_photo(request, home_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, home_id=home_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', home_id=home_id)
  
@login_required
def add_rent_review(request, rent_id):
  form = RentReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.rent_id = rent_id
    new_review.save()
  return redirect('rent_detail', rent_id=rent_id)

@login_required
def add_rent_tour(request, rent_id):
  form = RentTourForm(request.POST)
  print(form)
  if form.is_valid():
    new_tour = form.save(commit=False)
    new_tour.rent_id = rent_id
    new_tour.save()
  return redirect('rent_detail', rent_id=rent_id)

@login_required
def add_rent_photo(request, rent_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            RentPhoto.objects.create(url=url, rent_id=rent_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('rent_detail', rent_id=rent_id)

@login_required
def add_furniture_review(request, furniture_id):
  form = FurnitureReviewForm(request.POST)
  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.furniture_id = furniture_id
    new_review.save()
  return redirect('furniture_detail', furniture_id=furniture_id)

@login_required
def add_furniture_photo(request, furniture_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            FurniturePhoto.objects.create(url=url, furniture_id=furniture_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('furniture_detail', furniture_id=furniture_id)
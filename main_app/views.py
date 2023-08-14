from django.shortcuts import render, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Home, Rent, Furniture

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
    return render(request, 'homes/detail.html', {
        'home': home
        })

class HomeCreate(CreateView):
    model = Home
    fields = ['address', 'price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/homes'

class HomeUpdate(UpdateView):
    model = Home
    fields = ['address', 'price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/homes'

class HomeDelete(DeleteView):
    model = Home
    success_url = '/homes'

def rents_index(request):
    rents = Rent.objects.all()
    return render(request, 'rents/index.html', 
    { 
        'rents': rents
        }
    )

def rents_detail(request, rent_id):
    rent = Rent.objects.get(id=rent_id)
    return render(request, 'rents/detail.html', {
        'rent': rent
        })

class RentCreate(CreateView):
    model = Rent
    fields = ['address', 'monthly_price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/rents'

class RentUpdate(UpdateView):
    model = Rent
    fields = ['address', 'monthly_price', 'square_footage', 'beds', 'baths', 'home_type', 'description']
    success_url = '/rents'

class RentDelete(DeleteView):
    model = Rent
    success_url = '/rents'

def furnitures_index(request):
  furnitures = Furniture.objects.all()
  return render(request, 'furnitures/index.html', 
  { 
    'furnitures': furnitures
    }
)

def furnitures_detail(request, furniture_id):
  furniture = Furniture.objects.get(id=furniture_id)
  return render(request, 'furnitures/detail.html', {'furniture': furniture})


class FurnitureCreate(CreateView):
  model = Furniture
  fields = '__all__'
  success_url = '/furnitures'

class FurnitureUpdate(UpdateView):
  model = Furniture
  fields = ['furniture_type', 'price', 'color', 'length', 'width', 'height', 'description']
  success_url = '/furnitures'

class FurnitureDelete(DeleteView):
  model = Furniture
  success_url = '/furnitures'

def assoc_furniture(request, home_id, furniture_id):
  Home.objects.get(id=home_id).furnitures.add(furniture_id)
  return redirect('detail', home_id=home_id)

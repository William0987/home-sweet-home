from django.contrib import admin
from .models import Home, Rent, Furniture, Review, Tour, Photo, RentReview, RentTour, RentPhoto, FurnitureReview, FurniturePhoto

admin.site.register(Home)
admin.site.register(Rent)
admin.site.register(Furniture)
admin.site.register(Review)
admin.site.register(Tour)
admin.site.register(Photo)
admin.site.register(RentReview)
admin.site.register(RentTour)
admin.site.register(RentPhoto)
admin.site.register(FurnitureReview)
admin.site.register(FurniturePhoto)


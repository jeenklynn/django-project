from django.contrib import admin
from .models import Menu, Reservation, Gallery, Subscription, Chef, Blog, Contact, Order, OrderItem, ShippingAdress

@admin.register(Menu)
class Menus(admin.ModelAdmin):
  list_display = ['name', 'desc', 'kind', 'img', 'price']

@admin.register(Reservation)
class Reservations(admin.ModelAdmin):
  list_display = ['fullname', 'email', 'phone_number', 'people', 'date', 'time', 'message']

@admin.register(Gallery)
class Gallery(admin.ModelAdmin):
  list_display = ['img', 'type']

@admin.register(Subscription)
class Subscriptions(admin.ModelAdmin):
  list_display = ['email']

@admin.register(Chef)
class Chefs(admin.ModelAdmin):
  list_display = ['fullname', 'type', 'photo', 'facebook', 'twitter', 'linkedin']

@admin.register(Blog)
class Blogs(admin.ModelAdmin):
  list_display = ['title', 'author', 'banner', 'release_date', 'content']

@admin.register(Contact)
class Contact(admin.ModelAdmin):
  list_display = ['name', 'email', 'subject', 'message']

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAdress)


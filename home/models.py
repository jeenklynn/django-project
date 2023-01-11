from django.db import models
from django.contrib.auth.models import User as Customer

class Menu(models.Model):
  name = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)
  Kinds = models.TextChoices('Kinds','Breakfast Meals Snacks Desserts Drinks')
  kind = models.CharField(blank=True, choices=Kinds.choices, max_length=10)
  img = models.ImageField(blank=True, null=True)
  price = models.DecimalField(max_digits=8, decimal_places=2)

  def __str__(self):
    return self.name

class Reservation(models.Model): 
  fullname = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone_number = models.CharField(max_length=12)
  people = models.IntegerField()
  date = models.DateField()
  time = models.TimeField()
  message = models.TextField()

  def __str__(self):
    return self.fullname

class Gallery(models.Model): 
  img = models.ImageField(blank=True, null=True)
  Types = models.TextChoices('Types','Food Drink Restaurant Dinner Dessert')
  type = models.CharField(blank=True, choices=Types.choices, max_length=20)

  def __str__(self):
    return str(self.img)

class Subscription(models.Model): 
  email = models.EmailField(max_length=255)

  def __str__(self):
    return str(self.email)

class Chef(models.Model): 
  fullname = models.CharField(max_length=255)
  Types = models.TextChoices('Types','Head Pizza Grill Burger')
  type = models.CharField(blank=True, choices=Types.choices, max_length=20)  
  photo = models.ImageField(blank=True, null=True)
  facebook = models.CharField(max_length=255, null=True)
  twitter = models.CharField(max_length=255, null=True)
  linkedin = models.CharField(max_length=255, null=True)

  def __str__(self):
    return str(self.fullname)

class Blog(models.Model): 
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  banner = models.ImageField(blank=True, null=True)
  release_date = models.DateField()
  content = models.TextField()

  def __str__(self):
    return str(self.title)

class Contact(models.Model): 
  name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  subject = models.CharField(max_length=255)
  message = models.TextField()

  def __str__(self):
    return str(self.name)

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
  date_orderd = models.DateTimeField(auto_now_add=True)
  complete = models.BooleanField(default=False, null=True, blank=False)
  transaction_id = models.CharField(max_length=200, null=True)

  def __str__(self):
    return str(self.id)

  @property
  def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_total for item in orderitems])
    return total

  @property
  def get_cart_items(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total

class OrderItem(models.Model):
  product = models.ForeignKey(Menu, on_delete=models.SET_NULL, blank=True, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
  quantity = models.IntegerField(default=0, null=True, blank=True)
  date_added = models.DateTimeField(auto_now_add=True)

  @property
  def get_total(self):
    total = self.product.price * self.quantity
    return total

class ShippingAdress(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
  order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
  address = models.CharField(max_length=200, null=True)
  city = models.CharField(max_length=200, null=True)
  state = models.CharField(max_length=200, null=True)
  zipcode = models.CharField(max_length=200, null=True)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.address

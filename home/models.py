import unicodedata
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _

class Menu(models.Model):
  name = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)
  Kinds = models.TextChoices('Kinds','Breakfast Meals Snacks Desserts Drinks')
  kind = models.CharField(blank=True, choices=Kinds.choices, max_length=10)
  img = models.ImageField(upload_to='images/', default='images/item.jpg')
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
  name = models.CharField(max_length=255)
  img = models.ImageField(upload_to='images/', default='images/chef.png')
  Types = models.TextChoices('Types','Food Drink Restaurant Dinner Dessert')
  type = models.CharField(blank=True, choices=Types.choices, max_length=20)

  def __str__(self):
    return str(self.name)

class Subscription(models.Model): 
  email = models.EmailField(max_length=255)

  def __str__(self):
    return str(self.email)

class Chef(models.Model): 
  fullname = models.CharField(max_length=255)
  Types = models.TextChoices('Types','Head Pizza Grill Burger')
  type = models.CharField(blank=True, choices=Types.choices, max_length=20)  
  photo = models.ImageField(upload_to='images/', default='images/chef.jpg')
  facebook = models.CharField(max_length=255, null=True)
  twitter = models.CharField(max_length=255, null=True)
  linkedin = models.CharField(max_length=255, null=True)

  def __str__(self):
    return str(self.fullname)

class Blog(models.Model): 
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  banner = models.ImageField(upload_to='images/', default='images/blog.jpg')
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

class Cart(models.Model):
  creation_date = models.DateTimeField(verbose_name=_('creation date'))
  checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

  class Meta:
    verbose_name = _('cart')
    verbose_name_plural = _('carts')
    ordering = ('-creation_date',)

  def __unicode__(self):
      return unicodedata(self.creation_date)

class ItemManager(models.Manager):
  def get(self, *args, **kwargs):
    if 'product' in kwargs:
      kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
      kwargs['object_id'] = kwargs['product'].pk
      del(kwargs['product'])
    return super(ItemManager, self).get(*args, **kwargs)

  def filter(self, *args, **kwargs):
    if 'product' in kwargs:
      kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
      kwargs['object_id'] = kwargs['product'].pk
      del(kwargs['product'])
    return super(ItemManager, self).filter(*args, **kwargs)

class Item(models.Model):
  cart = models.ForeignKey(Cart, verbose_name=_('cart'), on_delete=models.CASCADE)
  quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
  unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
  # product as generic relation
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  object_id = models.PositiveIntegerField()

  objects = ItemManager()

  class Meta:
    verbose_name = _('item')
    verbose_name_plural = _('items')
    ordering = ('cart',)

def __unicode__(self):
  return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

def total_price(self):
  return self.quantity * self.unit_price
total_price = property(total_price)

# product
def get_product(self):
  return self.content_type.get_object_for_this_type(pk=self.object_id)

def set_product(self, product):
  self.content_type = ContentType.objects.get_for_model(type(product))
  self.object_id = product.pk

product = property(get_product, set_product)
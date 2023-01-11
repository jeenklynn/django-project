from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import login, authenticate
from home.forms import SignUpForm
from django.contrib.auth.decorators import login_required

#@login_required
def index(request):
  return render(request, "index.html")

@login_required
def orders(request):
  return render(request, "orders.html")

def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      raw_password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=raw_password)
      login(user)
      return redirect('index')
  else:
    form = SignUpForm()
  return render(request, 'registration/signup.html', {'form': form})

def about_us(request):
  return render(request, "about-us.html")

def blog(request):
  blog = Blog.objects.all()
  context = {
    'blogs': blog,
  }
  template = loader.get_template('blog.html')
  return HttpResponse(template.render(context, request))

def contact(request):
  contact = Contact.objects.all()
  context = {
    'contacts': contact,
  }
  template = loader.get_template('contact.html')
  return HttpResponse(template.render(context, request))

def gallery(request):
  gallery = Gallery.objects.all()
  context = {
    'galleries': gallery,
  }
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render(context, request))

def menu(request):
  menu = Menu.objects.all()
  context = {
    'menus': menu,
  }
  template = loader.get_template('menu.html')
  return HttpResponse(template.render(context, request))

def our_team(request):
  chef = Chef.objects.all()
  context = {
    'chefs': chef,
  }
  template = loader.get_template('our-team.html')
  return HttpResponse(template.render(context, request))

def reservation(request):
  reservation = Reservation.objects.all().values()
  context = {
    'reservations': reservation,
  }
  template = loader.get_template('reservation.html')
  return HttpResponse(template.render(context, request))

def cart(request):
  if request.user.is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
  else:
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0}
  context = {'items': items}
  template = loader.get_template('cart.html')
  return HttpResponse(template.render(context, request))

def checkout(request):
  if request.user_is_authenticated:
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
  else:
    order = {'get_cart_total': 0, 'get_cart_items': 0}
    items = []
  context = {'items':items, 'order': order}
  return render(request, 'checkout.html', context)

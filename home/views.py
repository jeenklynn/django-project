from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Menu, Blog, Contact, Gallery, Chef, Reservation
from django.contrib.auth import login, authenticate
from home.forms import SignUpForm

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

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
  return render(request, 'signup.html', {'form': form})

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def about_us(request):
  template = loader.get_template('about-us.html')
  return HttpResponse(template.render())

def blog(request):
  blog = Blog.objects.all().values()
  context = {
    'blogs': blog,
  }
  template = loader.get_template('blog.html')
  return HttpResponse(template.render(context, request))

def contact(request):
  contact = Contact.objects.all().values()
  context = {
    'contacts': contact,
  }
  template = loader.get_template('contact.html')
  return HttpResponse(template.render(context, request))

def gallery(request):
  gallery = Gallery.objects.all().values()
  context = {
    'galleries': gallery,
  }
  template = loader.get_template('gallery.html')
  return HttpResponse(template.render(context, request))

def menu(request):
  menu = Menu.objects.all().values()
  context = {
    'menus': menu,
  }
  template = loader.get_template('menu.html')
  return HttpResponse(template.render(context, request))

def our_team(request):
  chef = Chef.objects.all().values()
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
  return HttpResponse(template.render())
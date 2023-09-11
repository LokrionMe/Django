import logging
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import User, Product, Order
from .forms import UserForm, ProductForm, OrderForm

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'main.html')


def about(request):
    logger.debug('About page accessed')
    return render(request, 'about.html')


def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})


def all_users(request):
    users = User.objects.all()
    return render(request, 'all_users.html', {'users': users})


def delete_user(request, id):
    try:
        person = User.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/all_users")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def all_products(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})


def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return HttpResponseRedirect("/all_products")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
    

def add_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

def all_orders(request):
    orders = Order.objects.all()
    return render(request, 'all_orders.html', {'orders': orders})

def delete_order(request, id):
    try:
        order = Order.objects.get(id=id)
        order.delete()
        return HttpResponseRedirect("/all_orders")
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Order not found</h2>")

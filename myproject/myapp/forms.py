from django import forms
from .models import User, Product, Order

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "email", "number", "addres",]
        labels = {"name": "name", "email": "email","number": "number","addres": "addres",}

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "count", "image"]
        labels = {"name": "name", "description": "description","price": "price","count": "count","image":"image",}

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer", "products", "total_price",]
        labels = {"customer": "customer", "products": "products","total_price": "total_price",}

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_user/', views.add_user, name='add user'),
    path('all_users/', views.all_users, name='all users'),
    path("delete_user/<int:id>/", views.delete_user, name='delete user'),
    path('all_products/', views.all_products, name='all products'),
    path('add_product/', views.add_product, name='add product'),
    path("delete_product/<int:id>/", views.delete_product, name='delete product'),
    path('add_order/', views.add_order, name='add order'),
    path('all_orders/', views.all_orders, name='all orders'),
    path("delete_order/<int:id>/", views.delete_order, name='delete order'),
]

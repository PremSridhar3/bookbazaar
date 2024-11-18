from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/update/<int:order_id>/', views.update_cart, name='update_cart'),
    path('cart/delete/<int:order_id>/', views.remove_from_cart, name='remove_from_cart'),
]

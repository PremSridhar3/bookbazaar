from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from inventory.models import Book
from bookorder.models import BookOrder
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@login_required
def add_to_cart(request, book_id):
    if request.method == "POST":
        # Fetch the book object
        book = get_object_or_404(Book, book_id=book_id)
        
        # Check for an existing order
        existing_order = BookOrder.objects.filter(user=request.user, book=book, is_ordered=False).first()
        
        if existing_order:
            # If the order exists, increment the quantity
            existing_order.quantity += 1
            existing_order.save()
            messages.success(request, f'Updated quantity for {book.book_name} in your cart.')
        else:
            # If no existing order, create a new one
            BookOrder.objects.create(
                user=request.user,
                book=book,
                quantity=1,  # Default quantity
                is_ordered=False
            )
            messages.success(request, f'Added {book.book_name} to your cart.')
        
        return redirect('home')

@login_required
def cart_view(request):

    cart_items = BookOrder.objects.filter(user=request.user, is_ordered=False)
    
    return render(request, 'cart.html', {'cart_items': cart_items})

@login_required
def update_cart(request, order_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(BookOrder, cart_id=order_id)
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity += quantity
        cart_item.save()
        return redirect('cart')  # Redirect back to the cart page

@login_required
def remove_from_cart(request, order_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(BookOrder, cart_id=order_id)
        cart_item.delete()
        return redirect('cart')  # Redirect back to the cart page
from django.db import models
from django.conf import settings
from inventory.models import Book  # Assuming you have a Book model in the inventory app

class BookOrder(models.Model):
    cart_id = models.AutoField(primary_key=True)  # Automatically increments
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="orders")  # Assuming you have a Book model in the inventory app
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")  # Linking to the user model
    quantity = models.PositiveIntegerField(default=1)  # Default to 0
    is_ordered = models.BooleanField(default=False)  # Default to False
    ordered_date = models.DateTimeField(null=True, blank=True)  # Optional field, blank is True for forms

    def __str__(self):
        return f"Order {self.cart_id} - {self.book.title} - {self.user.username}"


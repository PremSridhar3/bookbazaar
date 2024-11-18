from django.db import models

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)  
    book_name = models.CharField(max_length=255) 
    author = models.CharField(max_length=255) 
    description = models.TextField()  
    genre = models.CharField(max_length=100)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.book_name

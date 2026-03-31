from django.db import models

STATUS = [
    (0, 'Inactive'),
    (1, 'Active'),
    (5, 'Deactivated'),
]

class userData(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=1)

class bookData(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    types = models.CharField(max_length=100)
    stock = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=1)
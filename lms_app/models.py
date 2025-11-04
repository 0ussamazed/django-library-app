from django.db import models
from django.utils import timezone
import random
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Book(models.Model):
    status_book = [
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),
    ]
    
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=250, null=True, blank=True)
    book_image = models.ImageField(upload_to='images', null=True, blank=True)
    author_image = models.ImageField(upload_to='images', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    retal_price_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    retal_period = models.IntegerField(null=True, blank=True)
    total_rental = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    isActive = models.BooleanField(default=True)
    status = models.CharField(max_length=50, choices=status_book, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True,blank=True)
    created_at = models.DateTimeField(default=timezone.now)  # التاريخ يتولد تلقائياً ولا يتعدل من الفورم

    # ✅ حقول الزبون (اختيارية)
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_phone = models.CharField(max_length=20, null=True, blank=True)
    client_address = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title

from django.db import models
from django.core.validators import MinValueValidator
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    stock_quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    image_urls = models.JSONField(default=list)  # Store as JSON array

    def add_to_inventory(self, quantity):
        self.stock_quantity += quantity
        self.save()

    def calculate_average_rating(self):
        return self.review_set.aggregate(models.Avg('rating'))['rating__avg']

from django.db import models
from .users import User

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def calculate_total(self):
        return sum(item.calculate_subtotal() for item in self.items.all())

from django.db import models
from django.utils.timezone import datetime

class Discount(models.Model):
    code = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=1, choices=[('P', 'Percentage'), ('F', 'Fixed')])
    value = models.DecimalField(max_digits=5, decimal_places=2)
    expiry_date = models.DateField()

    def apply_discount(self, price):
        if not self.is_valid():
            return price
        return price - (price * self.value / 100) if self.type == 'P' else max(0, price - self.value)

    def is_valid(self):
        return self.expiry_date >= datetime.date.today()
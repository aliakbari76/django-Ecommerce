from django.db import models
from .order import Order

class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def process_payment(self):
        # Logic to process payment
        self.status = 'Processed'
        self.save()


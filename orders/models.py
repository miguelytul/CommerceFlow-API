from django.db import models

# Create your models here.

class Order(models.Model):
  
   total = models.DecimalField(max_digits=10, decimal_places=2)
   status = models.CharField(
    max_length=10,
    choices=[
        ("pending", "pending"),
        ("paid", "paid"),
        ("cancelled", "cancelled"),
    ],
    default="pending"
)
      #False = pendente True = 
   created_at = models.DateTimeField(auto_now_add=True)

# from django.db import models
# from Ekartapp.models import Product
#
#
# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     address1 = models.CharField(max_length=255)
#     address2 = models.CharField(max_length=255)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     pincode = models.CharField(max_length=10)
#     order_id = models.CharField(max_length=100)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     payment_status = models.BooleanField(default=False)

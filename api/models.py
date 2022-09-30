from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    length = models.IntegerField(max_length=30)
    stock = models.BooleanField(max_length=30)
    color = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through = "CartProduct")


class CartProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    





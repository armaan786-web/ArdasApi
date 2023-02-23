from django.db import models
import math

# Create your models here.

class Product(models.Model):
    product_img = models.ImageField(upload_to='Product Image')
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    discount = models.IntegerField()
    color = models.CharField(max_length=100,null=True,blank=True)

    @property
    def selling_price(self):
        return math.ceil((int(self.price)*(self.discount))/100)



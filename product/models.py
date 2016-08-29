from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)


class Product(models.Model):
    name = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images', null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def get_price(self):
        return self.price


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
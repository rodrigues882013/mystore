from django.db import models
from product.models import Item


class Cart(models.Model):
    code = models.CharField(max_length=10)
    ship_value = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return str(self.cart.id)


class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __unicode__(self):
        return "Cart id: %s" % (self.id)

    @staticmethod
    def add_item_on_cart(item, cart):
        CartItem.objects.create(item=item, cart=cart)



from django.test import TestCase
from cart.models import Cart, CartItem
from product.models import Product, Item, Category


class CartTestCase(TestCase):

    def setUp(self):
        Cart.objects.create(code='AOOD11111', ship_value=20.00, total=40.00)
        category = Category.objects.create(name='General')
        product = Product.objects.create(name='Test product', category=category, price=20.00)
        Item.objects.create(product=product)

    def test_if_cart_was_created_with_successfull(self):
        cart = Cart.objects.get(code='AOOD11111')
        self.assertTrue(isinstance(cart, Cart))

    def test_add_item_on_cart(self):
        cart = Cart.objects.get(code='AOOD11111')
        product = Product.objects.get(name='Test product')
        item = Item.objects.get(product=product)
        CartItem.add_item_on_cart(item, cart)
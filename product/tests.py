from django.test import TestCase
from product.models import Category, Product, Item


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='General')

    def test_if_category_was_created_with_successful(self):
        category = Category.objects.get(name='General')
        self.assertTrue(isinstance(category, Category))


class ProductTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='General')
        Product.objects.create(name='Test product', category=category, price=20.00)

    def test_if_product_was_created_with_successfull(self):
        product = Product.objects.get(name='Test product')
        self.assertTrue(isinstance(product, Product))


class ItemTestCase(TestCase):
    def setUp(self):
        category = Category.objects.create(name='General')
        product = Product.objects.create(name='Test product', category=category, price=20.00)
        Item.objects.create(product=product)

    def test_if_item_was_created_with_successfull(self):
        p = Product.objects.get(name='Test product')
        item = Item.objects.get(product=p)
        self.assertTrue(isinstance(item, Item))

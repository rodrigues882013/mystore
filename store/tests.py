from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test import Client
from product.models import Product, Category

class StoreTestCase(TestCase):

    def setUp(self):
        Category.objects.create(name='T.I')
        Category.objects.create(name='Eletronics')
        Category.objects.create(name='Sports')
        Category.objects.create(name='Lifestyle')

        category = Category.objects.get(name='T.I')

        Product.objects.create(category=category, name="Hard drive", price=200.00)
        Product.objects.create(category=category, name="Monitor", price=200.00, sale_price=180.00)
        Product.objects.create(category=category, name="Motherboard", price=220.00, sale_price=120.00)
        Product.objects.create(category=category, name="VGA Nvidia", price=400.00)

    def test_index_page(self):
        url = reverse('store:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_if_index_page_has_item_list(self):
        url = reverse('store:index')
        response = self.client.get(url)
        item_list = response.context['items_list']
        self.assertIsNotNone(item_list)

    def test_if_index_page_has_product_list(self):
        url = reverse('store:index')
        response = self.client.get(url)
        item_list = response.context['items_list']

        self.assertTrue(item_list['products'])
        self.assertEqual(len(item_list['products']), 4)


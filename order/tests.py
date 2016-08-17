from django.test import TestCase
from order.models import Order
from cart.models import Cart
from django.contrib.auth.models import User
from account.models import Account


class OrderTestCase(TestCase):
    def setUp(self):
        cart = Cart.objects.create(code='AOOD11111', ship_value=20.00, total=40.00)
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        account = Account.objects.create(
            user=user,
            address='Bla bla bla',
            address2='Bla bla bla 2',
            city='Rio de Janeiro',
            country='Brazil',
            zipcode='21240-630',
            phone='4444-4444')

        Order.objects.create(cart=cart,
                             account=account,
                             order_code='ASDS12345')

    def test_if_order_was_created_with_successfull(self):
        order = Order.objects.get(order_code='ASDS12345')
        self.assertTrue(isinstance(order, Order))

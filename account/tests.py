from django.test import TestCase
from account.models import Account
from account.services import AccountService
from account.forms import AccountRegisterForm, AccountLoginForm, AccountUpdateForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class AccountTestCase(TestCase):

    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

        Account.objects.create(
            user=user,
            address='Bla bla bla',
            address2='Bla bla bla 2',
            city='Rio de Janeiro',
            country='Brazil',
            zipcode='21240-630',
            phone='4444-4444')

    def test_address_format(self):
        account = Account.objects.get(user=1)
        self.assertEqual(account.get_address(), 'Bla bla bla, Rio de Janeiro, Brazil, 21240-630')

    def test_if_account_was_created_with_successful(self):
        account = Account.objects.get(user=1)
        self.assertTrue(isinstance(account, Account))

    def test_home_account_view(self):
        url = reverse('account:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_account_view(self):
        url = reverse('account:login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_logout_account_view(self):
        url = reverse('account:logout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_account_view(self):
        url = reverse('account:register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_account_register_form(self):
        form_data = dict(first_name='First',
                         last_name='Last',
                         user_name='username',
                         email='user@gmail.com',
                         password='password',
                         confirm_password='password')

        form = AccountRegisterForm(form_data)
        self.assertTrue(form.is_valid())

    def test_account_update_form(self):
        form_data = dict(address='blablalb',
                         city='Rio de Janeiro',
                         country='Brazil',
                         zipcode='22222222',
                         phone='3333333')
        form = AccountUpdateForm(form_data)
        self.assertTrue(form.is_valid())

    def test_account_login_form(self):
        form_data = dict(user_name='username', password='12333')
        form = AccountLoginForm(form_data)
        self.assertTrue(form.is_valid())

    def test_account_service_create_account(self):
        result = AccountService.create_account(first_name='First',
                                               last_name='Last',
                                               user_name='username',
                                               email='user@gmail.com',
                                               password='password')

        self.assertTrue(result)






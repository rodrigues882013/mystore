import jwt

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from account.models import Account
from django.shortcuts import render



class AccountService(object):

    @staticmethod
    def create_account(**kwargs):
        user = User.objects.create_user(kwargs['user_name'], kwargs['email'], kwargs['password'])
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.save()

        t = Account.objects.create(user=user)

        print t
        return True

    def update_account(self, account, address=None, address2=None, zipcode=None, phone=None, city=None, country=None):
        pass


def require_loggin(function):
    def wrapped(request):
        if request.method == 'GET':
            token = request.GET['token']

            if token is not None:
                return render(request, 'account/home.html', {'token': token})

            return function(request)

    return wrapped


class AuthJWT(object):

    @staticmethod
    def _create_token(user_id):
        return "%s %s" % ("Bearer", jwt.encode(dict(user=user_id), 'secret', algorithm='HS256'))

    @classmethod
    def authenticate(cls, username, password):
        user = authenticate(username=username, password=password)

        if user is not None:
            token = cls._create_token(user.id)
        else:
            return False

        return token








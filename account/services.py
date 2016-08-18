import jwt
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from account.models import Account
from django.shortcuts import render


class AccountService(object):

    @staticmethod
    def create_account(**kwargs):
        user = User.objects.create_user(kwargs['user_name'], kwargs['email'], kwargs['password'])
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.save()

        Account.objects.create(user=user)
        return True

    @staticmethod
    def update_account(account, address=None, zipcode=None, phone=None, city=None, country=None):

        if address is not None:
            account.address = address

        if zipcode is not None:
            account.zipcode = zipcode

        if phone is not None:
            account.phone = phone

        if city is not None:
            account.city = city

        if country is not None:
            account.country = country

        account.save()

    @staticmethod
    def get_account(user_id):
        return Account.objects.get(user_id=user_id)


def require_loggin(function):

    def wrapped(request):

        if request.method == 'GET':
            token = request.GET.get('token')

            if token is None:
                response = HttpResponse(json.dumps({"error": "Not alowed"}))
                response.status_code = 405
                return response

        return function(request)

    return wrapped


class AuthJWT(object):

    @staticmethod
    def _create_token(user_id):
        return jwt.encode(dict(user=user_id), 'secret', algorithm='HS256')

    @staticmethod
    def decode_token(token):
        user = None
        if token is not None:
            claims = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = claims.get('user')

        return user

    @classmethod
    def authenticate(cls, username, password):
        user = authenticate(username=username, password=password)

        if user is not None:
            token = cls._create_token(user.id)
        else:
            token = False

        return token








import json
import logging

from django.shortcuts import render
from django.http import HttpResponse
from forms import AccountRegisterForm, AccountLoginForm, AccountUpdateForm
from services import AccountService, AuthJWT, require_loggin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


# Get an instance of a logger
logger = logging.getLogger(__name__)


@require_loggin
def home(request):
    token = request.GET['token']
    return render(request, 'account/home.html', dict(token=token))


def login(request):
    if request.method == 'POST':
        form = AccountLoginForm(request.POST)

        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']

            token = AuthJWT.authenticate(user_name, password)

            if token:
                url = "%s?token=%s" % (reverse('account:home'), token)
                return HttpResponseRedirect(url)
            else:
                response = HttpResponse()
                response.status_code = 404
                return response

        else:
            pass

    else:
        form = AccountLoginForm()

        return render(request, 'account/login.html', {'form': form})


@require_loggin
def logout(request):
    return HttpResponse("Account Logout")


def register(request):
    if request.method == 'POST':
        form = AccountRegisterForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password != confirm_password:
                pass

            AccountService.create_account(first_name=first_name,
                                          last_name=last_name,
                                          user_name=user_name,
                                          email=email,
                                          password=password)

            return render(request, 'account/register.html', {'regards': 'Thank for your register'})
    else:
        form = AccountRegisterForm()

    return render(request, 'account/register.html', {'form': form})


@require_loggin
def update(request):
    logger.info("Update view")
    token = None

    if request.method == 'POST':
        form = AccountUpdateForm(request.POST)

        if form.is_valid():
            token = request.META['QUERY_STRING'].split('=')[1]
            address = form.cleaned_data['address']
            city = form.cleaned_data['city']
            country = form.cleaned_data['country']
            zipcode = form.cleaned_data['zipcode']
            phone = form.cleaned_data['phone']
            user_id = AuthJWT.decode_token(token)
            account = AccountService.get_account(user_id)
            AccountService.update_account(account=account,
                                          address=address,
                                          city=city,
                                          country=country,
                                          zipcode=zipcode,
                                          phone=phone)
    else:
        token = request.GET['token']
        user_id = AuthJWT.decode_token(token)
        account = AccountService.get_account(user_id)

        form_data = dict(address=account.address,
                         city=account.city,
                         country=account.country,
                         zipcode=account.zipcode,
                         phone=account.phone)
        form = AccountUpdateForm(initial=form_data)
        print form

        logger.debug("Accound: %s", str(account))

    return render(request, 'account/update.html', {'form': form, 'token': token})

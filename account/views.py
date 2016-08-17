from django.shortcuts import render
from django.http import HttpResponse
from forms import AccountRegisterForm, AccountLoginForm, AccountUpdateForm
from services import AccountService, AuthJWT, require_loggin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


@require_loggin
def home(request):
    return render(request, 'account/home.html')


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
            pass

    else:
        form = AccountLoginForm()

        return render(request, 'account/login.html', {'form': form})


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

from django import forms


class AccountRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=120)
    user_name = forms.CharField(max_length=120)
    last_name = forms.CharField(max_length=120)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


class AccountUpdateForm(forms.Form):
    address = forms.CharField(max_length=120)
    city = forms.CharField(max_length=120)
    country = forms.CharField(max_length=120)
    zipcode = forms.CharField(max_length=120)
    phone = forms.CharField(max_length=120)


class AccountLoginForm(forms.Form):
    user_name = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput())


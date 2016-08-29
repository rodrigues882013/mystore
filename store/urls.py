from django.conf.urls import url
from . import views
from store.views import IndexView

app_name = 'store'

urlpatterns = [
    url(r'$', IndexView.as_view(), name='index')
]
from django.db import models
from django.conf import settings


class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=120)
    address2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    zipcode = models.CharField(max_length=25)
    phone = models.CharField(max_length=120)

    def __unicode__(self):
        return self.get_address()

    def get_address(self):
        return "%s, %s, %s, %s" % (self.address, self.city, self.country, self.zipcode)


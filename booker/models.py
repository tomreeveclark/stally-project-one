from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from decimal import Decimal

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="assoc_user")
    
    def __str__(self):
        return self.user.username
    

class Market(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, related_name="market_owner")

    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Market, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class Stall(models.Model):
    name = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, related_name="stall_owner")
    

    def __str__(self):
        return self.name
    
class Event(models.Model):
    market = models.ForeignKey(Market)
    date = models.DateField()

    def __str__(self):
        return self.market.name + ' ' + str(self.date)

class Application(models.Model):
    stall = models.ForeignKey(Stall)
    market = models.ForeignKey(Market)

    VALUE_CHOICES=(
        (None,'Respond (Accept/Decline)'),
        (True, 'Accept'),
        (False, 'Decline')
        )

    value = models.NullBooleanField(choices=VALUE_CHOICES, default=None, null=True, blank=True)

    def __str__(self):
        return self.stall.name + ' application to ' + self.market.name

class Booking(models.Model):
	stall = models.ForeignKey(Stall)
	market = models.ForeignKey(Market)

	VALUE_CHOICES=(
		(None,'Respond (Accept/Decline)'),
		(True, 'Accept'),
		(False, 'Decline')
		)

	value = models.NullBooleanField(choices=VALUE_CHOICES, default=None, null=True, blank=True)


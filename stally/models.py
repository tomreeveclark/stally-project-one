#from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from decimal import Decimal

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile")
    follows = models.ManyToManyField('Market', related_name="followedby")
    
    #website = models.URLField(blank=True)
    #picture = models.ImageField(upload_to='profile_images', blank=True)
    
    def __str__(self):
        return self.user.username
    

class Market(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=100, blank=True)
    
    lat = models.DecimalField(max_digits=10, decimal_places=7, default=Decimal('10.000000'))
    lng = models.DecimalField(max_digits=10, decimal_places=7, default=Decimal('10.000000'))
    
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
    market = models.ForeignKey(Market)
    
    #sub_user = models.ForeignKey(UserProfile, blank=True)
    
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Stall, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
        
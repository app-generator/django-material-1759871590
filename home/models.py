# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Bgp(models.Model):

    #__Bgp_FIELDS__
    ce hostname = models.CharField(max_length=255, null=True, blank=True)
    pe hostname = models.CharField(max_length=255, null=True, blank=True)
    ce ip address = models.CharField(max_length=255, null=True, blank=True)
    default-originate = models.BooleanField()

    #__Bgp_FIELDS__END

    class Meta:
        verbose_name        = _("Bgp")
        verbose_name_plural = _("Bgp")



#__MODELS__END

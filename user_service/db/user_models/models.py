# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=1024)
    password = models.CharField(max_length=256)
    mobile = models.CharField(max_length=12)
    city = models.CharField(max_length=256)


class Login(models.Model):
    user = models.ForeignKey(User)
    login_time = models.DateTimeField(auto_now_add=True)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=1024)
    middle_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    mobile = models.CharField(max_length=12)
    city = models.CharField(max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)


class Login(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=64, default=str(uuid.uuid4()), primary_key=True)
    is_active = models.BooleanField(default=True)
    login_time = models.DateTimeField(auto_now_add=True)
    logout_time = models.DateTimeField(null=True)

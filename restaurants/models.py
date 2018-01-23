# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class RestaurantType (models.Model):
    name = models.CharField(max_length=255)


class Restaurant (models.Model):
    name = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()
    description = models.TextField()
    type = models.ForeignKey(RestaurantType, on_delete=models.CASCADE)

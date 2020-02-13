# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import  Expese, Income

# Register your models here.

admin.site.register(Expese)
admin.site.register(Income)
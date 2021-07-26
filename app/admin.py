# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.apps import apps

for model in apps.get_app_config('app').models.values():
    admin.site.register(model)
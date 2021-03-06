# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 20:15
from __future__ import unicode_literals

from django.db import migrations
from django.db.migrations import RunPython
from django.db.utils import IntegrityError


def forward(apps, schema_editor):
    User = apps.get_model("users", "User")
    for user in User.objects.all():
        if True in {i.isupper() for i in user.username}:
            try:
                print("Lowercasing username %s" % user.username)
                User.objects.filter(id=user.id).update(username=user.username.lower())
            except IntegrityError:
                print("Can't lowercase username %s - clash with existing user!" % user.username)


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_max_length_of_username'),
    ]

    operations = [
        RunPython(forward, RunPython.noop)
    ]

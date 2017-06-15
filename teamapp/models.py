# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


class TeamMemberRole(models.Model):
    # id = models.IntegerField(primary_key=True)
    role_name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'role_master'


class TeamMember(models.Model):
    # Django provides an auto_increment id
    # id = models.AutoField(primary_key=True, blank=True)
    first_name = models.CharField(max_length=255, null=False, blank=True)
    last_name = models.CharField(max_length=255, null=False, blank=True)
    phone_number = models.CharField(max_length=10,
                                    validators=[
                                        RegexValidator(regex='^\d{10}$', message='Phone number must contain'
                                                                                 ' 10 digits',
                                                       code='invalid_phone_number')
                                    ],
                                    null=False,
                                    blank=True)
    email = models.EmailField(max_length=255, null=False, blank=True)
    role = models.ForeignKey(TeamMemberRole, on_delete=models.CASCADE, null=False, blank=True)

    class Meta:
        db_table = 'team_member'

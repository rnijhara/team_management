# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from teamapp.models import TeamMember, TeamMemberRole

admin.site.register(TeamMember)
admin.site.register(TeamMemberRole)

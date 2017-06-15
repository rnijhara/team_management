# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from teamapp.models import TeamMember
from teamapp.serializers import TeamMemberSerializer

from rest_framework import generics

# Using generic class-based views


class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class TeamMemberList(generics.ListCreateAPIView):

    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

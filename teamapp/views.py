# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from teamapp.models import TeamMember
from teamapp.serializers import TeamMemberSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TeamMemberDetail(APIView):

    def get_object(self, pk):
        try:
            return TeamMember.objects.get(pk=pk)
        except TeamMember.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        team_member = self.get_object(pk)
        serializer = TeamMemberSerializer(team_member)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        team_member = self.get_object(pk)
        serializer = TeamMemberSerializer(team_member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        team_member = self.get_object(pk)
        team_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamMemberList(APIView):

    def get(self, request, format=None):
        team_members = TeamMember.objects.all()
        serializer = TeamMemberSerializer(team_members, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeamMemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

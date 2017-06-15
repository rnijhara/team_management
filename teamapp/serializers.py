from teamapp.models import TeamMember, TeamMemberRole

from rest_framework import serializers


class TeamMemberSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=TeamMemberRole.objects.all())

    class Meta:
        model = TeamMember
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'email', 'role')

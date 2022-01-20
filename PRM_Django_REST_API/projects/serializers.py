from rest_framework import serializers
from users.serializers import UserProfileSerializer

from .models import Project, Risk


class BasicRiskSerializer(serializers.ModelSerializer):
    """
    Serializes Risk objects for display as nested objects for views pertaining to Projects
    """
    class Meta:
        model = Risk
        fields = ["id", "name"]


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializes Project objects in a way convenient for views pertaining to Projects - in other words, contains
    the full picture of a Project object rather than an abridged one
    """
    risks = BasicRiskSerializer(many=True, read_only=True)
    users_assigned = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "name", "description", "risks", "users_assigned"]


class BasicProjectSerializer(serializers.ModelSerializer):
    """
    Serializes Project objects for display as nested objects for views pertaining to Risks and possibly other
    """
    class Meta:
        model = Project
        fields = ["id", "name"]


class RiskSerializer(serializers.ModelSerializer):
    """
    Serializes Risk objects in a way convenient for views pertaining to Risks - in other words, contains
    the full picture of a Risk object rather than an abridged one
    """
    project = BasicRiskSerializer(many=False, read_only=False)
    background = serializers.CharField(source="get_background_display")
    priority = serializers.CharField(source="get_priority_display")
    probability_percentage = serializers.CharField(
        source="get_probability_percentage_display"
    )
    resolvers_assigned = UserProfileSerializer(many=True, read_only=True)
    change_history = serializers.ListField(source="get_change_history")

    class Meta:
        model = Risk
        fields = [
            "id",
            "name",
            "project",
            "background",
            "resolvers_assigned",
            "priority",
            "probability_percentage",
            "change_history",
        ]


class RiskSerializerForUpdateRequests(serializers.ModelSerializer):
    """
    Same as risk serializer - the difference is that it does not present the serialized versions of the IDs
    nested within (users, project) as does the main serializer (i.e. nested serialization)
    """
    background = serializers.CharField(source="get_background_display")
    priority = serializers.CharField(source="get_priority_display")
    probability_percentage = serializers.CharField(
        source="get_probability_percentage_display"
    )

    class Meta:
        model = Risk
        fields = '__all__'


class ProjectSerializerForUpdateRequests(serializers.ModelSerializer):
    """
    Same as project serializer - the difference is that it does not present the serialized versions of the IDs
    nested within (users, risks) as does the main serializer (i.e. no nested serialization)
    """
    class Meta:
        model = Project
        fields = '__all__'

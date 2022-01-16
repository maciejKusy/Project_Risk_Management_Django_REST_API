from rest_framework import serializers
from .models import Project, Risk
from users.serializers import UserProfileSerializer


class BasicRiskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Risk
        fields = ['id', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    risks = BasicRiskSerializer(many=True, read_only=True)
    users_assigned = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'risks', 'users_assigned']


class BasicProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name']


class RiskSerializer(serializers.ModelSerializer):
    project = BasicRiskSerializer(many=False, read_only=False)
    background = serializers.CharField(source='get_background_display')
    user_assigned = UserProfileSerializer(many=False, read_only=True)
    priority = serializers.CharField(source='get_priority_display')
    probability_percentage = serializers.CharField(source='get_probability_percentage_display')
    change_history = serializers.ListField(source='get_change_history')

    class Meta:
        model = Risk
        fields = ['id', 'name', 'project', 'background', 'user_assigned', 'priority', 'probability_percentage',
                  'change_history']


class RiskSerializerForUpdateRequests(serializers.ModelSerializer):

    class Meta:
        model = Risk
        fields = ['id', 'project', 'user_assigned']


class ProjectSerializerForUpdateRequests(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'risks', 'users_assigned']









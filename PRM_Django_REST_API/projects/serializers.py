from rest_framework import serializers
from .models import Project, Risk
from users.serializers import UserProfileSerializer


class RiskSerializer(serializers.ModelSerializer):
    background = serializers.CharField(source='get_background_display')
    user_assigned = UserProfileSerializer(many=False, read_only=True)
    priority = serializers.CharField(source='get_priority_display')
    probability_percentage = serializers.CharField(source='get_probability_percentage_display')

    class Meta:
        model = Risk
        fields = ['id', 'name', 'background', 'user_assigned', 'priority', 'probability_percentage']


class ProjectSerializer(serializers.ModelSerializer):
    risks = RiskSerializer(many=True, read_only=True)
    users_assigned = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'risks', 'users_assigned']


class DetailedRiskSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(many=False)
    background = serializers.CharField(source='get_background_display')
    user_assigned = UserProfileSerializer(many=False, read_only=True)
    priority = serializers.CharField(source='get_priority_display')
    probability_percentage = serializers.CharField(source='get_probability_percentage_display')
    change_history = serializers.ListField(source='get_change_history')

    class Meta:
        model = Risk
        fields = ['id', 'name', 'project', 'background', 'user_assigned', 'priority', 'probability_percentage',
                  'change_history']








from django.utils.datetime_safe import datetime
from rest_framework import serializers
from .models import Project, Risk


class RiskSerializer(serializers.ModelSerializer):
    background = serializers.CharField(source='get_background_display')
    user_assigned = serializers.StringRelatedField(many=False)
    priority = serializers.CharField(source='get_priority_display')
    probability_percentage = serializers.CharField(source='get_probability_percentage_display')

    class Meta:
        model = Risk
        fields = ['name', 'background', 'user_assigned', 'priority', 'probability_percentage']


class ProjectSerializer(serializers.ModelSerializer):
    risks = RiskSerializer(many=True, read_only=True)
    users_assigned = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['name', 'description', 'risks', 'users_assigned']
        depth = 1


class DetailedRiskSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(many=False)
    background = serializers.CharField(source='get_background_display')
    user_assigned = serializers.StringRelatedField(many=False)
    priority = serializers.CharField(source='get_priority_display')
    probability_percentage = serializers.CharField(source='get_probability_percentage_display')
    change_history = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Risk
        fields = ['id', 'name', 'project', 'background', 'user_assigned', 'priority', 'probability_percentage',
                  'change_history']

    @classmethod
    def get_change_history(cls, instance):
        history = instance.change_history.all().values()
        changes_list = list(history)
        irrelevant_changes = ['history_id', 'history_date']
        changes_descriptions = []
        for index, change in enumerate(changes_list):
            if index != 0:
                for key, value in change.items():
                    if changes_list[index-1][key] != changes_list[index][key]:
                        if key not in irrelevant_changes:
                            new_value = changes_list[index - 1][key]
                            old_value = changes_list[index][key]
                            timestamp = datetime.strftime(changes_list[index]['history_date'], '%d-%m-%Y, %H:%M:%S')
                            changes_descriptions.append(f'Change: {key} was changed from {old_value} to {new_value}'
                                                        f' on {timestamp}.')
        return changes_descriptions






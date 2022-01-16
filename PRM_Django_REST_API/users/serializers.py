from rest_framework import serializers
from .models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    username = serializers.CharField(source='__str__')

    class Meta:
        model = Profile
        fields = ['id', 'username', 'account_created']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['account_created'] = instance.account_created.strftime('%d-%m-%Y %H:%M')
        return representation



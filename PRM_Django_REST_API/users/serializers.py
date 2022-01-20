from rest_framework import serializers

from .models import Profile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Provides a serialized version of relevant user information.
    """
    id = serializers.PrimaryKeyRelatedField(read_only=True, many=False)
    username = serializers.CharField(source="__str__")

    class Meta:
        model = Profile
        fields = ["id", "username", "account_created"]

    def to_representation(self, instance):
        """
        Modifies the timestamp so that it is displayed in a more convenient way.
        :param instance: an instance of Profile model
        :return: serialized representation of said object
        """
        representation = super().to_representation(instance)
        representation["account_created"] = instance.account_created.strftime(
            "%d-%m-%Y %H:%M"
        )
        return representation

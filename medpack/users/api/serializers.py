from django.contrib.auth import get_user_model
from rest_framework import serializers
from medpack.users.models import UserProfile


User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=255,write_only=True,allow_null=True,allow_blank=True)
    class Meta:
        model = UserProfile
        fields=[
            "address",
            "phone",
            "is_completed",
            "name"
        ]
        read_only_fields=['is_completed']

    def update(self, instance, validated_data):
        name=validated_data.pop("name",None)
        if name:
            instance.user.name=name
            instance.user.save()

        return super(UserProfileSerializer, self).update(instance,validated_data)


class UserSerializer(serializers.ModelSerializer):
    profile=UserProfileSerializer(read_only=True)
    class Meta:
        model = User
        fields = ["username", "name","email","profile"]
        ref_name="Medpack User"

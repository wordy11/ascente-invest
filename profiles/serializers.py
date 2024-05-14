from rest_framework import serializers
from.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'date_of_birth', 'bio', 'country', 'city', 'address', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

    def update(self, instance, validated_data):
        # Update the instance with the validated data
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.country = validated_data.get('country', instance.country)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        # instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.save()
        return instance


class ProfileReadSerializer(ProfileSerializer):
    user = serializers.ReadOnlyField()

    class Meta(ProfileSerializer.Meta):
        read_only_fields = ProfileSerializer.Meta.read_only_fields + ['user']

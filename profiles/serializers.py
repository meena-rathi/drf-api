from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile_id')
    profile_image= serializers.ReadOnlyField(source='onwer.profile.image.url')

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'image size'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'longer image'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'longer image.'
            )
        return value
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'content', 'image', 'is_owner','image_filter'
        ]
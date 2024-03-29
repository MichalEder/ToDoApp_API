from rest_framework import serializers

from ToDoApp_api import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'surname', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
           email=validated_data['email'],
           name=validated_data['name'],
           surname=validated_data['surname'],
           password=validated_data['password'],
       )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class TaskSerializer(serializers.ModelSerializer):
    """Serializes a task object"""

    class Meta:
        model = models.Task
        fields = ('id', 'user', 'email', 'title', 'description', 'completed', 'created')
        extra_kwargs = {'user': {'read_only': True},
                        'email': {'read_only': True}}


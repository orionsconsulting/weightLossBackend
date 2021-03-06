from rest_framework import serializers
from weightLoss.models import WeightTracker, User


class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    firstName = serializers.CharField(max_length=30)
    lastName = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.firstName = validated_data.get('name', instance.firstName)
        instance.lastName = validated_data.get('description', instance.lastName)
        instance.save()
        return instance


class WeightTrackerSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    date = serializers.DateField()
    weight = serializers.DecimalField(decimal_places=2, max_digits=5)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('name', instance.date)
        instance.weight = validated_data.get('description', instance.weight)
        instance.save()
        return instance

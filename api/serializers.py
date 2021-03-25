from rest_framework import serializers

from .models import Table, Leg, Feet


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name', 'leg']


class LegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leg
        fields = ['id', 'name', 'feet']


class FeetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feet
        fields = ('id', 'name', 'width', 'length', 'radius')

    def validate(self, data):
        if data['radius']:
            if data['width'] or data['length']:
                raise serializers.ValidationError(
                    "A foot with a radius must not have length or width")
        if data['length']:
            if not data['width']:
                raise serializers.ValidationError(
                    "A foot with a length must also have a width")
        if data['width']:
            if not data['length']:
                raise serializers.ValidationError(
                    "A foot with a width must also have a length ")
        return data



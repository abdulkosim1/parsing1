from rest_framework import serializers 
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    # city = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Department
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    # departments = DepartmentSerializer(many=True, read_only=True)

    # area = serializers.SlugRelatedField(slug_field='title', read_only=True)
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['area'] = instance.area.title
        return representation

    class Meta:
        model = City
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    # cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    # area = AreaSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
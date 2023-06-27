from rest_framework import serializers 
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['region'] = instance.region.title
        return representation

    class Meta:
        model = City
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class TicketSerialier(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['executant'] = instance.executant.email
        representation['region'] = instance.region.title
        representation['area'] = instance.area.title
        representation['city'] = instance.city.title
        representation['department'] = instance.department.title
        representation['transaction'] = instance.transaction.title
        return representation

    class Meta:
        model = Ticket
        fields = '__all__'

class OfflineTicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = OffileTicket
        fields = '__all__'

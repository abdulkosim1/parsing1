
from .models import City, Area, Transaction, Department, Region
from rest_framework.generics import ListAPIView
from .serializers import CitySerializer, AreaSerializer, TransactionSerializer, DepartmentSerializer, RegionSerializer


class GetCityListAPIView(ListAPIView): # get запрос на просмотр всех городов
    queryset = City.objects.all()
    serializer_class = CitySerializer

class GetAreaListAPIView(ListAPIView): # get запрос на просмотр всех районов
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
class GetDepartmentListAPIView(ListAPIView): # get запрос на просмотр всех филиалов
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class GetRegionListAPIView(ListAPIView): # get запрос на просмотр всех регионов
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class GetTransactionListAPIView(ListAPIView): # get запрос на просмотр всех операций
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
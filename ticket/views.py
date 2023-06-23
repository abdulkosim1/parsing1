from .models import City, Area, Transaction, Department, Region, Ticket
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CitySerializer, AreaSerializer, TransactionSerializer, DepartmentSerializer, RegionSerializer, TicketSerialier
from rest_framework.permissions import IsAuthenticated

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


class GetTicketListAPIView(ListAPIView): # get запрос на просмотр всех билетов
    queryset = Ticket.objects.all()
    serializer_class = TicketSerialier


class CreateTicketCreateAPIView(CreateAPIView): # post запрос на создание билета
    queryset = Ticket.objects.all()
    serializer_class = TicketSerialier
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


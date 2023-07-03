from .models import City, Area, Transaction, Department, Region, Ticket, OffileTicket, TicketQueue, Window
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from .serializers import CitySerializer, AreaSerializer, TransactionSerializer, DepartmentSerializer, RegionSerializer, TicketSerialier, OfflineTicketSerializer, QueueSerializer, WindowSerializer, TicketActivationCodeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .permissions import IsOwner, IsWorker
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import generics

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

class RetrieveUpdateDestroyAPIViewTicketAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet): # update, delete запрос на билеты
    queryset = Ticket.objects.all()
    serializer_class = TicketSerialier
    lookup_field='id'
    permission_classes = [IsAuthenticated, IsOwner]

class ChangeTicketAPIViewTicketAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                                    viewsets.GenericViewSet): # update, delete запрос на билеты
    queryset = Ticket.objects.all()
    serializer_class = TicketSerialier
    lookup_field='id'
    permission_classes = [IsAuthenticated, IsWorker]

    def perform_create(self, serializer):
        serializer.save(executant=self.request.user)

class GetMyTicketListAPIView(ListAPIView): # get запрос на просмотр бронированного билета
    queryset = Ticket.objects.all()
    serializer_class = TicketSerialier
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user.id)


class CreateOfflineTicketListCreateAPIView(ListCreateAPIView):
    queryset = OffileTicket.objects.all()
    serializer_class = OfflineTicketSerializer

class QueueListCreateAPIView(generics.ListCreateAPIView):
    queryset = TicketQueue.objects.order_by('created_at').filter(is_served=True)
    serializer_class = QueueSerializer

class WindowListCreateAPIView(generics.ListCreateAPIView):
    queryset = Window.objects.all()
    serializer_class = WindowSerializer

class WindowRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Window.objects.all()
    serializer_class = WindowSerializer

    def perform_update(self, serializer):
        window = serializer.save()
        if not window.is_available and not window.current_ticket:
            window.current_ticket = self.get_next_ticket(window)
            window.save()

    def get_next_ticket(self, window):
        queue = TicketQueue.objects.filter(operator=window.operator, is_served=False).order_by('created_at').first()
        if queue:
            queue.is_served = True
            queue.save()
            return queue.ticket
        return None


class TicketListAPIView(ListAPIView):
    serializer_class = TicketSerialier

    def get_queryset(self):
        query = self.request.query_params.get('query', '')  # Get query parameter
        queryset = Ticket.objects.all()  # Apply filtering logic
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['offline_tickets'] = OffileTicket.objects.all()  # Include data from OfflineTicket model
        return context
    
class ActivationAPIView(APIView):
    def get(self, request, activation_code):
        try:
            ticket = Ticket.objects.get(activation_code=activation_code)
            ticket.status = True
            ticket.activation_code = ''
            ticket.save()
            return Response('Активация билета прошла успешно.', status=200)
        except Ticket.DoesNotExist:
            return Response('Активационный код уже был использован.', status=400)

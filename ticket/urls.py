from django.urls import path
from .views import *

urlpatterns = [
    path('queue/', QueueListCreateAPIView.as_view()),
    path('window/', WindowListCreateAPIView.as_view(), name='window-list-create'),
    path('window/<int:pk>/', WindowRetrieveUpdateDestroyAPIView.as_view(), name='window-retrieve-update-destroy'),

    path('get_area/', GetAreaListAPIView.as_view()),
    path('get_city/', GetCityListAPIView.as_view()),
    path('get_region/', GetRegionListAPIView.as_view()),
    path('get_department/', GetDepartmentListAPIView.as_view()),
    path('get_transaction/', GetTransactionListAPIView.as_view()),

    path('activate/<str:activation_code>/', ActivationAPIView.as_view()),
    path('get_ticket/', GetTicketListAPIView.as_view()),
    path('get_my_ticket/', GetMyTicketListAPIView.as_view()),
    path('create_ticket/', CreateTicketCreateAPIView.as_view()),
    path('offline_ticket/', CreateOfflineTicketListCreateAPIView.as_view()),
    path('change_ticket/<int:id>/', RetrieveUpdateDestroyAPIViewTicketAPIView.as_view({'put': 'update','patch': 'partial_update','delete': 'destroy'})),
    path('process_ticket/<int:id>/', ChangeTicketAPIViewTicketAPIView.as_view({'put': 'update','patch': 'partial_update','delete': 'destroy'})),



]



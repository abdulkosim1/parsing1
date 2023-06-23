from django.urls import path
from .views import *

urlpatterns = [
    path('get_area/', GetAreaListAPIView.as_view()),
    path('get_city/', GetCityListAPIView.as_view()),
    path('get_region/', GetRegionListAPIView.as_view()),
    path('get_department/', GetDepartmentListAPIView.as_view()),
    path('get_transaction/', GetTransactionListAPIView.as_view()),


]



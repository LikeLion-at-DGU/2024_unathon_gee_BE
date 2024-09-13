from django.urls import path
from .views import AlarmListCreateAPIView, AlarmRetrieveUpdateDestroyAPIView, FortuneGetAPIView

urlpatterns = [
    path('alarms/', AlarmListCreateAPIView.as_view(), name='alarm-list-create'),
    path('alarms/<int:pk>/', AlarmRetrieveUpdateDestroyAPIView.as_view(), name='alarm-detail'),
    path('fortune/', FortuneGetAPIView.as_view(), name='fortune'),
]
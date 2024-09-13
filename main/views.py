import random
from rest_framework import generics, mixins
from .models import Alarm, Fortune
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import AlarmSerializer, FortuneSerializer
from rest_framework.filters import OrderingFilter

class AlarmListCreateAPIView(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer
    filter_backends = [OrderingFilter]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

class AlarmRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                        mixins.UpdateModelMixin,
                                        mixins.DestroyModelMixin,
                                        generics.GenericAPIView):
    queryset = Alarm.objects.all()
    serializer_class = AlarmSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    
class FortuneGetAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Fortune.objects.all()
    serializer_class = FortuneSerializer
    
    def get(self, request, *args, **kwargs):
        fortune = Fortune.objects.all()
        random_fortune = random.choice(fortune)
        
        serializer = self.get_serializer(random_fortune)
        
        return Response(serializer.data)
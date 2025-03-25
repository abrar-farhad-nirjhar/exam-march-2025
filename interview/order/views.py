from django.shortcuts import render
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrderListApiView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        start = self.request.query_params.get("start")
        embargo = self.request.query_params.get("embargo")

        if start and embargo:
            queryset = queryset.filter(
                start_date__gte=start
            ).filter(embargo_date__lte=embargo)

        return queryset

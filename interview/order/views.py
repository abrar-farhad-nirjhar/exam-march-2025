from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class OrdersOnTag(APIView):
    def get(self, request, tag=None):
        if not tag:
            return Response(
                data={
                    "error": "tag must be provided"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            order_tag = OrderTag.objects.get(name=tag)

            orders = order_tag.orders.all()
            return Response(
                data=OrderSerializer(orders, many=True).data,
                status=status.HTTP_200_OK
            )

        except OrderTag.DoesNotExist:
            return Response(
                data={
                    "error": f"OrderTag {tag} does not exist."
                },
                status=status.HTTP_404_NOT_FOUND
            )

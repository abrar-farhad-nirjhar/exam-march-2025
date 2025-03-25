
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrdersOnTag


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('orders-on-tag/<str:tag>', OrdersOnTag.as_view(), name="orders-on-tag"),
]

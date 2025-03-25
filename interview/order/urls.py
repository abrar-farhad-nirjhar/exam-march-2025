
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, TagsOnOrdersView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('tags-on-orders/<pk>', TagsOnOrdersView.as_view(), name='tags-on-orders')
]

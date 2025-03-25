
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderListApiView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('filtered', OrderListApiView.as_view(), name="order-list-filterable")

]

from django.urls import path
from .views import CartView, AddToCartView, RemoveFromCartView, PlaceOrderView, MyOrdersView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/remove/<int:item_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('orders/place/', PlaceOrderView.as_view(), name='place-order'),
    path('orders/my-orders/', MyOrdersView.as_view(), name='my-orders'),
]
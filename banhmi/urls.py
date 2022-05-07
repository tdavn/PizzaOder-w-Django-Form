from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('order/', views.order, name='order'),
    path('banhmis', views.banhmis, name='banhmis'),
    path('order/edit_<int:pk>', views.edit_order, name='edit_order'),
]
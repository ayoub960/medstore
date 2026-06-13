from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('medicine/<slug:slug>/', views.medicine_detail, name='medicine_detail'),
    path('order/<int:medicine_id>/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),

    # NEW PAGES
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
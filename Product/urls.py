from django.urls import path

from Product import views

urlpatterns = [
    path('', views.products.as_view(), name='products'),
    path('brand/<slug:brand>/', views.products.as_view(), name='brand'),
    path('cat/<slug:cat>/', views.products.as_view(), name='category'),
    path('<slug:slug>/', views.product_details.as_view(), name='product_detail'),


]
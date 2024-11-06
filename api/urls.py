from django.urls import path
from .views import ProductListAPIView, ProductDeleteAPIView, ProductDetailAPIView, ProductUpdateAPIView, \
    ProductCreateAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='list'),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', ProductDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='update'),
    path('create/', ProductCreateAPIView.as_view(), name='create'),
]

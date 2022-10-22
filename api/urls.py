from django.urls import path
from .views import ProductAPIView  # ProductCreateView

urlpatterns = [
    path('product-create/', ProductAPIView.as_view()),

]

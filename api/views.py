from django.forms import model_to_dict
from django.shortcuts import render
from .models import Product
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateProductSerializer


# class ProductCreateView(APIView):
#     """Creating APIView for product"""
#
#     def post(self, request):
#         product = CreateProductSerializer(data=request.data)
#         if product.is_valid():
#             product.save()
#         return Response(status=201)

class ProductAPIView(APIView):
    # model_to_dict

    def get(self):
        pass

    def post(self, request):
        product = Product.objects.create(
            title=request.data.get('title'),
            price=request.data.get('price')
        )
        return Response({"text": model_to_dict(product)})

    def put(self, request):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

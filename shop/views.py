from ast import Mod
from unicodedata import category
from rest_framework.views import APIView
from rest_framework.response import Response

from shop.models import Article, Category, Product
from shop.serializers import CategorySerialiser, ProductSerializer, ArticleSerializer

class CategoryAPIView(APIView):
    
    def get(self, *args, **kwargs):
        #queryset
        categories = Category.objects.all()
        serializer= CategorySerialiser(categories, many=True)#many: pour qu'il puisse generer pusieur
        return Response(serializer.data)


class ProductAPIView(APIView):
    
    def get(self, *args, **kwargs):
        #queriset
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data) 
    

class ArticleAPIView(APIView):
     def get(self, *args, **kwargs):
        #queriset
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
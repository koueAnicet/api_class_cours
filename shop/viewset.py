from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet
from shop.models import Article, Category, Product
from shop.serializers import CategorySerialiser, ProductSerializer, ArticleSerializer


class CategoryViewset(ModelViewSet):
    
    serializer_class=CategorySerialiser
    
    def get_queryset(self):
        return Category.objects.all()

class ProductViewset(ModelViewSet):
    
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all()


class ArticleViewset(ModelViewSet):
    serializer_class = ArticleSerializer
    
    def get_queryset(self):
        return Article.objects.all()
    
       
# class CategoryAPIView(APIView):
    
#     def get(self, *args, **kwargs):
#         #queryset
#         categories = Category.objects.all()
#         serializer= CategorySerialiser(categories, many=True)#many: pour qu'il puisse generer pusieur
#         return Response(serializer.data)


# class ProductAPIView(APIView):
    
#     def get(self, *args, **kwargs):
#         #queriset
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data) 
    

# class ArticleAPIView(APIView):
#      def get(self, *args, **kwargs):
#         #queriset
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
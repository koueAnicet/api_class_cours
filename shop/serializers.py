from rest_framework.serializers import ModelSerializer

from shop.models import Article, Category, Product

class CategorySerialiser(ModelSerializer):
    
    class Meta:
        model = Category
        fields =['id', 'name', 'active','date_created', 'date_updated']
    
        
class ProductSerializer(ModelSerializer):
    
    class Meta:
        model= Product
        fields = ['id', 'name','category', 'date_created','date_updated']


class ArticleSerializer(ModelSerializer):
    
    class Meta:
        model = Article
        fields=['id', 'name', 'description','active', 'product']
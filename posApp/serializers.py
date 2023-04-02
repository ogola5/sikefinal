from .models import Category, Products, Sales, salesItems
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description', 'date_added', 'date_updated']

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['code', 'category_id', 'name', 'description','price', 'status','date_added', 'date_updated']  

class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = ['code', 'sub_total', 'grand_total', 'tax_amount','tax', 'tendered_amount','amount_change', 'date_added', 'date_updated']  

class salesItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = salesItems
        fields = ['sale_id', 'product_id', 'price', 'qty','total']  
from rest_framework.serializers import ModelSerializer 
from .models import Book, BookCategory

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book 
        fields = ['id', 'title', 'price']
    
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save() 
        return instance 
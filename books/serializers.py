from rest_framework import serializers
from books.models import Book,Carts,Reviews



class CartSerializer(serializers.ModelSerializer):
    book=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)

    class Meta:
        model=Carts
        fields=["book","user","date"]
    def create(self, validated_data):
        user=self.context.get("user")
        book=self.context.get("book")
        return Carts.objects.create(**validated_data,user=user,book=book)

class ReviewSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    book=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Reviews
        fields="__all__"

    def create(self, validated_data):
        user=self.context.get("user")
        book=self.context.get("book")
        return Reviews.objects.create(**validated_data,user=user,book=book)

class BookSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    book_reviews=ReviewSerializer(read_only=True,many=tuple)
    avg_rating=serializers.CharField(read_only=True)

    class Meta:
        model=Book
        fields="__all__"


    
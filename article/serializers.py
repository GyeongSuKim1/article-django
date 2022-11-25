from rest_framework import serializers
from article.models import Article as ArticleModel

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleModel
        # fields = "__all__"
        fields = [
            "id", 
            "title", 
            "content", 
            
            "created_at", 
            "updated_at",
            ]
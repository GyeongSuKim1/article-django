from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, exceptions

from article.serializers import ArticleSerializer
from article.models import Article as ArticleModel


# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = ArticleModel.objects.all().order_by('-created_at')
        serialized_data = ArticleSerializer(articles, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print(f"| data : {data}")
        article_serializer = ArticleSerializer(data=data)
        print(f"| serializer : {article_serializer}")

        try:
            article_serializer.is_valid()
            article_serializer.save()
            return Response(
                {"message": "게시글이 작성되었습니다."}, status=status.HTTP_200_OK
                )
        
        except exceptions.ValidationError:
            return Response(
                {"message": "제목이나 내용을 확인해주세요."}, status=status.HTTP_400_BAD_REQUEST
                )

        except:
            print(f"Error : {article_serializer.errors}")
            return Response(
                article_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
    
    def put(self, request, article_id):
        data = request.data
        article = ArticleModel.objects.get(id=article_id)
        article_serializer = ArticleSerializer(article, data=data, partial=True)
        
        try: 
            article_serializer.is_valid()
            article_serializer.save()
            return Response(
                {"message": "게시글이 수정되었습니다."}, status=status.HTTP_200_OK
                )
            
        except ArticleModel.DoesNotExist:
            return Response(
                {"message": "존재하지않는 게시글입니다."}, status=status.HTTP_404_NOT_FOUND
            )
            
        except:
            return Response(
                article_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
    
    
    def delete(self, request, article_id):
        article = ArticleModel.objects.get(id=article_id)
        
        try:
            article.delete()
            return Response(
                {"message": "게시글이 삭제되었습니다."}, status=status.HTTP_200_OK
                )
        except ArticleModel.DoesNotExist:
            return Response(
                {"message": "존재하지않는 게시글입니다."}, status=status.HTTP_404_NOT_FOUND
                )


class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = ArticleModel.objects.get(id=pk)
        article_serializer = ArticleSerializer(article, many=False).data
        
        return Response (article_serializer)
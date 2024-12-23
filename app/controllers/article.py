from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.serializers.article import ArticleSerializer
from app.models.article import Article

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def article(request):
    if request.method == 'GET':
        objs = Article.objects.all()
        serializer = ArticleSerializer(objs, many = True)
        return Response(serializer.data)
    # return Response({"message": "this is a sample article!"})
    elif request.method == 'POST':
        data = request.data
        serializer = ArticleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        data = request.data
        serializer = ArticleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    elif request.method == 'PATCH':
        data = request.data
        obj = Article.objects.get(id = data['id'])
        serializer = ArticleSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        article_id = request.data.get('id')
        if not article_id:
            return Response({"detail": "No article ID provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            article_obj = Article.objects.get(id=article_id)
            article_obj.delete()  # Delete the article
            return Response({"detail": "Article deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Article.DoesNotExist:
            return Response({"detail": "Article not found."}, status=status.HTTP_404_NOT_FOUND)
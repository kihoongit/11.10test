from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from articles.models import Article
from rest_framework.generics import get_object_or_404
from articles.serializers import ArticlesSerializer
from drf_yasg.utils import swagger_auto_schema,no_body

class ArticleList(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticlesSerializer(articles,  many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticlesSerializer)
    def post(self, request, format=None):
        
        serializer = ArticlesSerializer(data = request.data) # 작성된 데이터를 serializer에 반영한다.
        print(serializer.data)
        if serializer.is_valid(): # 해당 데이터를 검증
           serializer.save() #데이터 DB에 저장.

           return Response(serializer.data, status=status.HTTP_201_CREATED) # 해당 시리얼라이즈에 저장한 데이터,상태를 리스폰스.
        else:
           print(serializer.errors)
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 해당 시리얼라이즈의 에러,상태를 리스폰스.

@api_view(['GET','PUT','DELETE','POST']) #참조한다
def article_view(request, article_id):
    if request.method == 'GET': # Read
        # articles = Article.object.all(id=article_id)
        article = get_object_or_404(Article,id=article_id) # get_object_xxx를 호출하는데 없으면, Http404 예외
        serializer = ArticlesSerializer(article) #serializer에 해당 article 값을 가져옴
        return Response(serializer.data, status=status.HTTP_200_OK) #위의 가져온 article.data를 띄워주고 상태 성공적인 200 상태메세지를 띄워줌

    elif request.method == 'PUT': # Create,Update
        article = get_object_or_404(Article, id=article_id) # get_object_xxx를 호출하는데 없으면, Http404 예외
        serializer = ArticlesSerializer(article, data = request.data) # #serializer에 해당 article 값을 가져옴
        if serializer.is_valid(): # 가져온 데이터를 검증,확인함.
            serializer.save() #상태 저장
            return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE': #Delete
        article = get_object_or_404(Article, id=article_id) # get_object_xxx를 호출하는데 없으면, Http404 예외
        article.delete() #해당 DB 삭제
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST': # Create
        # articles = Article.object.all(id=article_id)
        serializer = ArticlesSerializer(data = request.data) # get_object_xxx를 호출하는데 없으면, Http404 예외
        if serializer.is_valid(): # 해당 데이터를 검증
            serializer.save() #데이터 DB에 저장.
            return Response(serializer.data, status=status.HTTP_201_CREATED) # 해당 시리얼라이즈에 저장한 데이터,상태를 리스폰스.
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 해당 시리얼라이즈의 에러,상태를 리스폰스.


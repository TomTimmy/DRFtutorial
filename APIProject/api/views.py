import re
from django.db.models import manager
from rest_framework import serializers
from django.shortcuts import render, HttpResponse
from rest_framework.utils import serializer_helpers
from .models import Article
from .serializers import ArticleModelSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from django.shortcuts import get_object_or_404
""" 
# # 장고로 프론트엔드를 한다면, 이렇게 render 함수를 쓰면된다.
# def Index(request):
#     return render (request, 'index.html')

# ? 장고로 "백엔드"를 한다면. 요렇게!
def Index(request):
    return HttpResponse("It is working!") #! 이렇게 함수를 작성해도, url로 mapping 하지 않으면 작동하지 않는다.

# @csrf_exempt #? <== pk(id)로 게시글 확인하려면 필요함... csrf 란?: https://namu.wiki/w/CSRF
# def article_list(request):
#     #get all articles
#     if request.method == "GET":
#         articles = Article.objects.all()
#         serializer = ArticleModelSerializer(articles, many=True) # ? articles 가 Query Set 이기 때문에, many=True 를 써준다!
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = ArticleModelSerializer(data=data) 
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)

# ? decolator 사용하기. decolator: https://www.django-rest-framework.org/tutorial/2-requests-and-responses/#wrapping-api-views
# ? 또한, JsonResponse 대신 Response 를 사용했다.
@api_view(['GET', 'POST'])
def article_list(request):
    #get all articles
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleModelSerializer(articles, many=True) # ? articles 가 Query Set 이기 때문에, many=True 를 써준다!
        return Response(serializer.data) # ? JsonResponse 대신 Response 사용함.

    elif request.method == "POST":
        serializer = ArticleModelSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def article_details(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)

#     except Article.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = ArticleModelSerializer(article)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT': #? 업데이트 할때는 PUT !!! POST 는 만들때!
#         data = JSONParser().parse(request)
#         serializer = ArticleModelSerializer(article, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         else:
#             return JsonResponse(serializer.errors, status=400)
 
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204) # ? 제거되었으니 데이터 없음을 표출.


@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleModelSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT': #? 업데이트 할때는 PUT !!! POST 는 만들때!
        serializer = ArticleModelSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED_)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # ? 제거되었으니 데이터 없음을 표출.
 """


# # ?  Class-based Views 연습.  Class-based Views: https://www.django-rest-framework.org/tutorial/3-class-based-views/
from rest_framework.decorators import APIView
# class ArticleList(APIView):
#     def get(self, requset):
#         articles = Article.objects.all()
#         serializer = ArticleModelSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, requset):
#         serializer = ArticleModelSerializer(data=requset.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# class ArticleDetails(APIView):
#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)
  
#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
   
#     def get(self, request, id):
#         articles = self.get_object(id)
#         serializer = ArticleModelSerializer(articles)
#         return Response(serializer.data)

#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleModelSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # ?  mixins 연습.  Using mixins: https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
# class ArticleList(generics.GenericAPIView, mixins.ListModelMixin,
# mixins.CreateModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleModelSerializer
    
#     def get(self, request):
#         return self.list(request)
        
#     def post(self, request):
#         return self.create(request)

# class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, 
# mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleModelSerializer

#     lookup_field = 'id' #? <== Solution to following Error: Expected view ArticleDetails to be called with a URL keyword argument named "pk". Fix your URL conf, or set the `.lookup_field` attribute on the view correctly.

#     def get(self, request, id):
#         return self.retrieve(request, id=id)

#     def put(self, request, id):
#         return self.update(request, id=id)

#     def delete(self, request, id):
#         return self.destroy(request, id=id)

# # ? ViewSet 과 Router 연습
# class ArticleViewSet(viewsets.ViewSet):

#     def list(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleModelSerializer(articles, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ArticleModelSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else: 
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleModelSerializer(article)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleModelSerializer(article, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else: 
#             return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# # ? Generic ViewSet 연습
# class ArticleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
# mixins.CreateModelMixin, 
# mixins.RetrieveModelMixin,
# mixins.UpdateModelMixin,
# mixins.DestroyModelMixin):
#     queryset = Article.objects.all()
#     serializer_class = ArticleModelSerializer #? () 가 없음을 주지할 것.

# ? Model ViewSet 연습
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer
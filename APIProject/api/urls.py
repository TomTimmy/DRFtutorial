
from django.urls import path, include
from rest_framework import routers
# from .views import article_list, article_details, 
# from .views import ArticleList, ArticleDetails
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

# ? router 사용하기
router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')

#! url로 mapping 하기. 방법2: 앱마다 따로 빼기.
urlpatterns = [
    # path('articles/', article_list),
    # path('articles/<int:pk>/', article_details),
    # path('articles/', ArticleList.as_view()), # ?  Class-based Views 사용시엔, .as_view() 를 꼭 붙여줘야함.
    # path('articles/<int:id>/', ArticleDetails.as_view()), 
    # ? router 사용하기
    path('', include(router.urls)),
]

"""APIProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""  

from django.contrib import admin
from django.urls import path, include
from rest_framework import parsers
# #! url로 mapping 하기. 방법1.
# from api.views import Index

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', Index),
# ]

#! url로 mapping 하기. 방법2: 따로 뺀것(앱/urls.py) 사용하기.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
]
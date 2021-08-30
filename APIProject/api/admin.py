from django.contrib import admin

# Register your models here.
# ? 만든 model 즉, 데이터베이스를 admin 패널에 등재하려면 여기서 코딩한다. 
# # ? 방법1. 아래처럼 하면 된다.
# from .models import Article
# admin.site.register(Article)

# ? 방법2. class 제작
from .models import Article
@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    # ? Decorationg ㅎㅎ 진짜 너무 쉽당.
    list_filter = ('title', 'description')
    list_display = ('title', 'description')
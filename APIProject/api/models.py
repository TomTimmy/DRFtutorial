from django.db import models
from django.db.models.base import Model

# Create your models here.
# ? model 은 그냥 데이터베이스 이다!
# ? model 을 수정한 다음에는, 꼭 항상 migration 해줘야 한다!
# ! migration 했는데 변화가 없다면, INSTALLED_APPS 에 앱이 추가되어있는지 확인해볼것!

class Article(models.Model):
    # ! id 는 항상 자동으로 생성된다! 코딩해줄 필요없음. 그리고 id 는 primary key 임.
    title = models.CharField(max_length=100)
    description = models.TextField()

    #? Article 글의 제목을 title로 지정하기!
    def __str__(self):
        return self.title
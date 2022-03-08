#ブログポストを定義する
#他のファイルから必要な部分をimportする
from django.conf import settings
from django.db import models
from django.utils import timezone

#クラスを定義する
class Post(models.Model):
  #フィールド
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  publised_date = models.DateTimeField(blank=True, null = True)

  #ブログを公開するメソッド
  def publish(self):
    self.publised_date = timezone.now()
    self.save()

  #
  def __str__(self):
    return self.title
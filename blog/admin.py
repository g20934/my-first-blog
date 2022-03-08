#ポストを追加、編集、削除する
from django.contrib import admin
from .models import Post

#モデルをAdminページ（管理画面）上で見えるようにする
admin.site.register(Post)

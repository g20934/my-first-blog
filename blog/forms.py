from django import forms
from .models import Post
class PostForm(forms.ModelForm):
  
  class Meta:
    model = Post                  #使用するモデルを決める
    fields = ('title', 'text')    #フォームのフィールドに何を置くか
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
  #公開したポストをpublised_dateで並び替えたクエリセットを取得する
  posts = Post.objects.filter(publised_date__lte=timezone.now()).order_by('publised_date')
  return render(request, 'blog/post_list.html', {'posts':posts})#前のpostsは名前、後ろのpostsは値（クエリセット）

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post})
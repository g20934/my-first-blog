from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
# Create your views here.
def post_list(request):
  #公開したポストをpublised_dateで並び替えたクエリセットを取得する
  posts = Post.objects.filter(publised_date__lte=timezone.now()).order_by('publised_date')
  return render(request, 'blog/post_list.html', {'posts':posts})#前のpostsは名前、後ろのpostsは値（クエリセット）

def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
  if request.method == "POST": #全てのフォームデータが入力された状態でビューに戻ってくるとき
    #フォームのデータを使ってPostFormを構築する
    form = PostForm(request.POST)
    if form.is_valid(): #フォームの値が有効なら
      #Postモデルはまだデータベースに保存しない
      post = form.save(commit=False)
      #投稿の筆者はリクエストしたuserにする
      post.author = request.user
      #公開日を設定
      post.publised_date = timezone.now()
      #Postをデータベースに保存する
      post.save()
      #新しく作成されたポストのpost_detailページに移動する
      return redirect('post_detail', pk=post.pk)
  else:                        #最初にページにアクセスしてきたとき
    form = PostForm() #空白のフォームを作る
  return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
  #編集したいPOSTを取得する
  post = get_object_or_404(Post, pk=pk)
  if request.method == "POST":
    #フォームを保存する
    form = PostForm(request.POST, instance=post)
    if form.is_valid():
      post = form.save(commit=False)
      post.author = request.user
      post.publised_date = timezone.now()
      post.save()
      return redirect('post_detail', pk=post.pk)
  else:
    #編集するためにフォームを開く
    form = PostForm(instance=post)
  return render(request, 'blog/post_edit.html', {'form': form})
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentForm

# Create your views here.

class PostView(View):
    def get(self, request): # метод get отпровляет запрос на сервер 
        posts = Post.objects.all() # получаем все записи из БД
        return render(request,'main/index.html', {'post_list': posts }) # отрисовываем шаблон с контекстом


class PostComment(View):
    # отдельная страница для коментирования 
    def get(self, request, pk):
        post = Post.objects.get(id=pk) # получаем запись по id
        return render(request,'main/postComent.html', {'post': post }) # отрисовываем шаблон с контекстом


def about(request):
    return render(request, 'main/about.html')

def postFun(request):
    return render(request, 'main/post.html')

class AddComments(View):
     # добавляем новый коментарий к посту
     def post(self, request, pk):
         form = CommentForm(request.POST) # получаем все данные от нашего пользователя 
         if form.is_valid(): # проверяем корректность введенных данных
            form = form.save(commit=False)
            form.post_id = pk
            form.save() # сохраняем в БД
         return redirect(f"/{pk}") # перенаправляем на главную страницу



def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR') # получаеv ip address
    if x_forwarded_for: # если есть ip adress
        ip = x_forwarded_for.split(',')[0] 
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request) # получаем ip address клиента
        try:
            like = Likes.objects.get(ip=ip_client, pos_id=pk) # проверяем, если уже лайкнул клиент
        except Likes.DoesNotExist:
            like = Likes(ip=ip_client, pos_id=pk)
            like.save()
        return redirect(f"/{pk}") # перенаправляем на главную страницу
    

class DeLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request) # получаем ip address клиента
        try:
            like = Likes.objects.get(ip=ip_client, pos_id=pk) # проверяем, если уже лайкнул клиент
            like.delete()
        except Likes.DoesNotExist:
            pass
        return redirect(f"/{pk}") # перенаправляем на главную страницу
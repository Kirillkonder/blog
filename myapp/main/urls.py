from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.PostView.as_view(), name='index'), #переход на галвную страницу
    path("<int:pk>/", views.PostComment.as_view()), # получаем id каждого поста  
    path("post/", views.postFun, name="post"),
    path("about/", views.about, name="about"),
    path("review/<int:pk>/", views.AddComments.as_view(), name="add_comments"),  # добавляем новый коментарий к посту
    path("<int:pk>/add_likes/", views.AddLike.as_view(), name="add_likes"),
    path("<int:pk>/del_likes/", views.DeLike.as_view(), name="del_likes"),
]

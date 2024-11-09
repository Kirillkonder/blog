from django.contrib import admin
from .models import Post, Comments #испорта нашей первой моедли

# фалй для импорта моделей 

@admin.register(Post)# указываем какую  именном модель мы регестрируем 
class Postadmin(admin.ModelAdmin):
    list_display = ('title', 'author') # поля которые будут отображаться в админке 



@admin.register(Comments)# указываем какую  именном модель мы регестрируем 
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post') # поля которые будут отображаться в админке 


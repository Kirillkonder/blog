# файл для проверки - заполнил ли пользовтель форму как надо 
from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta: # класс мета используеться для хранения информации
        model = Comments # модель для которой создаем форму
        fields = ('name', 'email', 'text_comments')
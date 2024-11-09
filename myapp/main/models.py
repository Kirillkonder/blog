from django.db import models

# фалйл для созданяи моеделй для бд 

# создания модели для постов 
class Post(models.Model): # обращения к родительскому класу чтобы наследовать все настройки 
    # данные о посте
    title = models.CharField('Заголовк записи', max_length=100) # фиксируем длину нашего поля 
    description = models.TextField('Описание') # поле для записи 
    author = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публицкации") 
    img = models.ImageField('Изооброжения', upload_to='media') # позволяте добовлять изооброжения 

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

# создания моделй для коментариев 
class Comments(models.Model):
     email = models.EmailField() # указаня email
     name = models.CharField('Имя пользователя', max_length=30)
     text_comments = models.TextField("Текст коментария", max_length=2000)
     post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE) # связь с постом

     def __str__(self):
        return f'{self.name}, {self.post}'

     class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


# создания модели для лайков
class Likes(models.Model):
     ip = models.CharField('IP-адрес', max_length=100)
     pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE) # связь с постом


    
    
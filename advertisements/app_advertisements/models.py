from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

# Заголовок
# Описание
# Цена
# Торг
# Дата создания
# Дата обновления

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    negotiable = models.BooleanField("торг", help_text="Отметьте, если уместен торг")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("изображение", upload_to="advertisements/")
    user = models.ForeignKey(User, verbose_name="пользователь", on_delete=models.CASCADE)

    @admin.display(description='дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
    
    @admin.display(description='дата последнего обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisements(id = {self.id}, title = {self.title}, price = {self.price})"
    
    class Meta:
        db_table = "advertisements"

    @admin.display(description='изображение')
    def image_display(self):
        if self.image:
            return format_html(
                '<img src="{}" style="width: 55px;">', self.image.url
            )
        else:
            return 'No Image'

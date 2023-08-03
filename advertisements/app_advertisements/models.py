from django.db import models

#   заголовок 
#   описание
#   цена
#   торг
#   дата создания
#   дата обновления данных о заказе

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_digits=10, decimal_places=2)
    negotiable = models.BooleanField("торг", help_text="Отметьте, если уместен торг")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"


from django.db import models
from datetime import datetime



class Phone(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images', blank=True)
    release_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    lte_exists = models.BooleanField(default=0)
    slug = models.SlugField(max_length=255, unique=True, blank=False)

# изменение стандартного имени таблицы (стандартное "имя проекта-имя класса", т.е. phones-phone)
    class Meta:
        db_table = "Phone"


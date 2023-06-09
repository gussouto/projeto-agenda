from django.db import models
from django.utils import timezone

# id (primary key - automático)
# fisrt_name (string), last_name (string), phone (string)
# email (email), create_date (date), description (text)
# category (foreign key), show (boolean), owner(foreign key)
# picture (image)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

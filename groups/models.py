from django.db import models

# Create your models here.
class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    # created_at = data e tempo, sendo preenchida
    # automaticamente com o datetime em que o objeto foi criado.

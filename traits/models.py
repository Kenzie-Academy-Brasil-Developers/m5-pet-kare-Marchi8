from django.db import models

# Create your models here.
class Trait(models.Model):
    # name = string, tamanho máximo 20, único
    name = models.CharField(max_length=20, unique=True)
    # Uma característica (trait)
    # pode estar ligada a vários pets
    # assim como um pet pode possuir várias características.
    # pets = models.ManyToManyField("pets.Pet", related_name="traits")

from django.db import models

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    weight = models.FloatField()
    sex = models.CharField(default="Not Informed")
    # somente dentre as opções Male, Female e Not Informed.


# Um grupo (group) pode ter vários pets atrelados a ele,
# porém um pet somente poderá estar conectado a um grupo.

# Uma característica (trait) pode estar ligada a vários pets
# assim como um pet pode possuir várias características.

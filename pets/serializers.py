from rest_framework import serializers
from groups.serializers import GroupSerializer

from pets.models import Sex
from traits.serializers import TraitSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.ChoiceField(
        choices=Sex.choices,
        default=Sex.Not_Informed,
    )
    group = GroupSerializer()
    traits = TraitSerializer(many=True)
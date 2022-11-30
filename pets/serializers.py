from rest_framework import serializers
from groups.serializers import GroupSerializer
from pets.models import Pet, Sex
from groups.models import Group
from traits.models import Trait
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

    def create(self, validated_data: dict) -> Pet:
        pet = Pet.objects.create(**validated_data)
        return pet

    def update(self, instance, validated_data: dict):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

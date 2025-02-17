from rest_framework import serializers

from coffee.apps.product.models import CoffeeMachine, CoffeePod


class CoffeeMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = "__all__"


class CoffeePodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePod
        fields = "__all__"

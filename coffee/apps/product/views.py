from rest_framework.generics import ListAPIView

from coffee.apps.product.models import CoffeeMachine, CoffeePod
from coffee.apps.product.serializers import CoffeeMachineSerializer, CoffeePodSerializer


class CoffeeMachineView(ListAPIView):
    serializer_class = CoffeeMachineSerializer
    queryset = CoffeeMachine.objects.all()
    filterset_fields = [
        "product_type",
        "water_line_compatible",
        "model_type",
    ]


class CoffeePodView(ListAPIView):
    serializer_class = CoffeePodSerializer
    queryset = CoffeePod.objects.all()
    filterset_fields = [
        "product_type",
        "coffee_flavor",
        "pack_size",
    ]

from django.urls import path

from coffee.apps.product.views import CoffeeMachineView, CoffeePodView

urlpatterns = [
    path("machines/", CoffeeMachineView.as_view(), name="machines"),
    path("pods/", CoffeePodView.as_view(), name="pods"),
]

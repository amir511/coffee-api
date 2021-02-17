from django.contrib import admin

from coffee.apps.product.models import CoffeeMachine, CoffeePod

admin.site.register((CoffeeMachine, CoffeePod))

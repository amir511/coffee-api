from django.db import models


class CoffeeMachine(models.Model):
    class ProductType(models.TextChoices):
        COFFEE_MACHINE_LARGE = "large", "Coffee machine large"
        COFFEE_MACHINE_SMALL = "small", "Coffee machine small"
        ESPRESSO_MACHINE = "espresso", "Espresso machine"

    class ModelType(models.TextChoices):
        BASE_MODEL = "base", "Base"
        PREMIUM_MODEL = "premium", "Premium"
        DELUXE_MODEL = "deluxe", "Deluxe"

    SKU_number = models.CharField(max_length=6, unique=True)
    product_type = models.CharField(choices=ProductType.choices, max_length=20)
    water_line_compatible = models.BooleanField()
    model_type = models.CharField(choices=ModelType.choices, max_length=15)

    def __str__(self):
        return self.SKU_number


class CoffeePod(models.Model):
    class ProductType(models.TextChoices):
        COFFEE_POD_LARGE = "large", "Coffee pod large"
        COFFEE_POD_SMALL = "small", "Coffee pod small"
        ESPRESSO_POD = "espresso", "Espresso pod"

    class CoffeeFlavor(models.TextChoices):
        COFFEE_FLAVOR_VANILLA = "vanilla", "Vanilla"
        COFFEE_FLAVOR_CARAMEL = "caramel", "Caramel"
        COFFEE_FLAVOR_PSL = "psl", "Psl"
        COFFEE_FLAVOR_MOCHA = "mocha", "Mocha"
        COFFEE_FLAVOR_HAZELNUT = "hazelnut", "Hazelnut"

    class PackSize(models.TextChoices):
        ONE_DOZEN = "1", "One dozen"
        THREE_DOZEN = "3", "Three dozen"
        FIVE_DOZEN = "5", "Five dozen"
        SEVEN_DOZEN = "7", "Seven dozen"

    SKU_number = models.CharField(max_length=6, unique=True)
    product_type = models.CharField(choices=ProductType.choices, max_length=20)
    coffee_flavor = models.CharField(choices=CoffeeFlavor.choices, max_length=25)
    pack_size = models.CharField(choices=PackSize.choices, max_length=12)

    def __str__(self):
        return self.SKU_number

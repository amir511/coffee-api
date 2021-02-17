from django.db import models


class CoffeeMachine(models.Model):
    class ProductType(models.TextChoices):
        COFFEE_MACHINE_LARGE = "coffe_machine_large", "Coffee machine large"
        COFFEE_MACHINE_SMALL = "coffe_machine_small", "Coffee machine small"
        ESPRESSO_MACHINE = "espresso_machine", "Espresso machine"

    class ModelType(models.TextChoices):
        BASE_MODEL = "base_model", "Base model"
        PREMIUM_MODEL = "premium_model", "Premium model"
        DELUXE_MODEL = "deluxe_model", "Deluxe model"

    SKU_number = models.CharField(max_length=6)
    product_type = models.CharField(choices=ProductType.choices, max_length=20)
    water_line_compatible = models.BooleanField()
    model_type = models.CharField(choices=ModelType.choices, max_length=15)

    def __str__(self):
        return self.SKU_number


class CoffeePod(models.Model):
    class ProductType(models.TextChoices):
        COFFEE_POD_LARGE = "coffe_pod_large", "Coffee pod large"
        COFFEE_POD_SMALL = "coffe_pod_small", "Coffee pod small"
        ESPRESSO_POD = "espresso_pod", "Espresso pod"

    class CoffeeFlavor(models.TextChoices):
        COFFEE_FLAVOR_VANILLA = "coffee_flavor_vanilla", "Coffee flavor vanilla"
        COFFEE_FLAVOR_CARAMEL = "coffee_flavor_caramel", "Coffee flavor caramel"
        COFFEE_FLAVOR_PSL = "coffee_flavor_psl", "Coffee flavor psl"
        COFFEE_FLAVOR_MOCHA = "coffee_flavor_mocha", "Coffee flavor mocha"
        COFFEE_FLAVOR_HAZELNUT = "coffee_flavor_hazelnut", "Coffee flavor hazelnut"

    class PackSize(models.TextChoices):
        ONE_DOZEN = "one_dozen", "One dozen"
        THREE_DOZEN = "three_dozen", "Three dozen"
        FIVE_DOZEN = "five_dozen", "Five dozen"
        SEVEN_DOZEN = "seven_dozen", "Seven dozen"

    SKU_number = models.CharField(max_length=6)
    product_type = models.CharField(choices=ProductType.choices, max_length=20)
    coffee_flavor = models.CharField(choices=CoffeeFlavor.choices, max_length=25)
    pack_size = models.CharField(choices=PackSize.choices, max_length=12)

    def __str__(self):
        return self.SKU_number

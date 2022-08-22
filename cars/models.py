"""Models of cars app"""

from django.db import models


class Car(models.Model):
    """Car model"""

    reg_number = models.CharField(
        "Регистрационный номер вместе с регионом",
        max_length=30,
    )

    model = models.CharField(
        "Модель",
        max_length=255,
    )

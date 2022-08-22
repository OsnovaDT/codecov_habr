"""Config of cars app"""

from django.apps import AppConfig


class CarsConfig(AppConfig):
    """Config class"""

    default_auto_field = 'django.db.models.BigAutoField'

    name = 'cars'

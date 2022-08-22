"""Tests for models from cars app"""

from django.test import TestCase

from cars.models import Car


class CarTests(TestCase):
    """Tests for Car model"""

    def test_verbose_name(self) -> None:
        """Test verbose_name attr"""

        self.assertEqual(
            Car._meta.get_field('reg_number').verbose_name,
            "Регистрационный номер вместе с регионом",
        )

        self.assertEqual(
            Car._meta.get_field('model').verbose_name,
            "Модель",
        )

    def test_max_length(self) -> None:
        """Test max_length attr"""

        self.assertEqual(Car._meta.get_field('reg_number').max_length, 30)

        self.assertEqual(Car._meta.get_field('model').max_length, 255)

from unittest import TestCase
from parameterized import parameterized

class TestParameterized(TestCase):
    @parameterized.expand([
        ("01", 1, 2, 3),
        ("02", 2, 3, 5),
        ("03", 3, 5, 8),
    ])
    def test_add(self, name, a, b, expected):
        self.assertEqual(a + b, expected)
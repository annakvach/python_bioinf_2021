import unittest
from math import pi
from circle import circle_area

class Test_circle_area(unittest.TestCase):
  # setUp method is overridden from the parent class TestCase
  # def setUp(self):
    # self.circle = circle_area(radius)

  # смотрим правильно ли вообще вычисляется площадь
  def test_area(self):
    self.assertEqual(circle_area(3), pi*3**2)
    self.assertEqual(circle_area(1), pi)
    self.assertEqual(circle_area(0), 0)
    self.assertEqual(circle_area(2.5), pi*2.5**2)

  # посмотрим, выбрасываются ли исключения для отрицательных радиусов
  def test_values(self):
    self.assertRaises(ValueError, circle_area, -2)
    self.assertRaises(ValueError, circle_area, -1)

  # выбрасываются исключения у несовместимости типов
  def test_types(self):
    self.assertRaises(TypeError, circle_area, 'str')
    self.assertRaises(TypeError, circle_area, [5])
    self.assertRaises(TypeError, circle_area, [5, 8])
    self.assertRaises(TypeError, circle_area, True)
    self.assertRaises(TypeError, circle_area, 'dgsdv+54l')

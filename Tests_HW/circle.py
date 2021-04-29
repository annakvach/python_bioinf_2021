from math import pi

def circle_area(radius):
  if radius < 0:
    raise ValueError('Radius can`t be negative')
  if type(radius) not in [int, float]:
    raise TypeError('Radius must be non-negative real number only (int or float)')
  return pi * radius ** 2



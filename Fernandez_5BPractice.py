##Robert Fernandez
##Complete
##Calculate the area of a circle from a random radius. 

import math
import random

def area_of_circle(radius):
  return math.pi * radius ** 2

def main():
  radius = random.uniform(1.0, 100.0)
  area = area_of_circle(radius)
  print(f'The radius is: {radius:,.2f} and the area is: {area:,.2f}')

if __name__ == '__main__':
  main() 

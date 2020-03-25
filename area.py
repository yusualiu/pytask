from math import pi

def calculateArea():
  radius = input('Please input your circle radius: ')
  radius = int(radius) #convert string to number
  area = pi * (radius**2) # square the radius and multiplied pi
  area = round(area,3) # round the value to 3 decimal places
  return area



print(f'The area of your circle is {calculateArea()}')
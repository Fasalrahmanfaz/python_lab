from my_package.basic_operation import arithmetic
from my_package.basic_operation import area

print("arithmetic operation")
print("5+3=",arithmetic.add(5,3))
print("10-7=",arithmetic.substract(10,7))
print("5*3=",arithmetic.multiply(5,3))
print("8/2=",arithmetic.divide(8,2))
print("8/0=",arithmetic.divide(8,0))

print("\n area calculation:")
print("rectangle (lenght=5,width=3):",area.rectangle_area(5,3))
print("circle radius=7):",area.circle_area(7))
print("triangle(base=4,height=5):",area.triangle_area(4,5))

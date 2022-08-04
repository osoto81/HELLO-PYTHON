from Circle import Circle


circle1 = Circle(1,10,"Blue",True)

circle2 = Circle(2,8,"Yellow",True)

circle3 = Circle(3,17,"Red",False)

# print("Circle 1 circumfrance is : " + (3.14 * 2 * circle1radius))
# print("Circle 2 circumfrance is : " + (3.14 * 2 * circle1radius))
# print("Circle 3 circumfrance is : " + (3.14 * 2 * circle1radius))

print("Circle 1 circumfrance is : " + circle1.circumfrence())
print("Circle 2 circumfrance is : " + circle2.circumfrence())
print("Circle 3 circumfrance is : " + circle3.circumfrence())
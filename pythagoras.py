import math

perpendicular = int(input("Enter the value of perpendicular: "))
base = int(input("Enter the value of base: "))

hypo = math.sqrt((perpendicular**2 + base**2))
print(f"The Hypotenuse of base {base} and perpendicualr {perpendicular} is {hypo}")
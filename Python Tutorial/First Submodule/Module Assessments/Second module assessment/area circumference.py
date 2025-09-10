import math
def get_positive_float(radius):
    value = float(input(radius))
    if value > 0:
        return value
    else:
        print("Radius must be greater than zero.")
radius = get_positive_float("Enter radius of the circle: ")
area = radius**2 * math.pi
print(f"The area of the circle is {area}.")
circumference = radius * 2 * math.pi
print(f"The circumference of the circle is {circumference}.")
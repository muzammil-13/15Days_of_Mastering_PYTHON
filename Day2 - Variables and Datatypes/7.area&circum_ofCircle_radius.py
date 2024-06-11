"""
Calculate the area and circumference(perimeter) of a circle given its
radius)
"""
radius=int(input("Radius of the circle: "))

area=3.14*(radius**2)
print(f"Area of the circle's radius {radius}: {area:.2f}")

circum=(2*3.14)*radius
print(f"Circumference of the circle with radius {radius}: {circum:.2f}")

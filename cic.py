import math

def get_circumference(radius):
    return 2 * math.pi * radius

# Example use:
r = float(input("Enter radius: "))
print(f"Circumference: {get_circumference(r):.2f}")

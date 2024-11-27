feet_inches = input("Enter feet and inches: ")

def parse(feet_inches):
    feet = float(feet_inches[0])
    inches = float(feet_inches[1:].strip())
    return (feet, inches)


def convert(feet, inches):
    meter = feet* 0.3048 + inches* 0.0254
    return meter


i,j = parse(feet_inches)
result = convert(i,j)

# print(result)
if result <1:
    print("Kid is too small for the ride")
else:
    print("Kid can ride")
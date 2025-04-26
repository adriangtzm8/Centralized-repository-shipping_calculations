# Shipping Cost Calculator

## Input package weight and shipping rate
distance = float(input("Enter the distance the package is traveling"))
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate * distance

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")

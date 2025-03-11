def compute_mpg(miles, gallons):
  if gallons == 0:
      return 0.0  # Avoid division by zero
  return miles / gallons

trip_count = 0

print("Enter trip details:")

while True:
  try:
      destination = input("Enter destination city: ")
      miles = float(input("Enter miles traveled: "))
      gallons = float(input("Enter gallons used: "))

      mpg = compute_mpg(miles, gallons)
      trip_count += 1

      print(f"\nDestination: {destination}")
      print(f"Miles Traveled: {miles}")
      print(f"Miles Per Gallon: {mpg:.2f}\n")
  except ValueError:
      print("Invalid input. Please enter valid numbers for miles and gallons.")

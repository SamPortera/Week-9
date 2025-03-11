def compute_total(quantity, price):
    total = quantity * price
    if total > 100000.00:  # Checking if total exceeds $100,000 for discount
        total *= 0.90  # Applying a 10% discount
    return total

# Get user input
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per unit: "))

# Compute total
total_price = compute_total(quantity, price)

# Display results
print("\nSummary")
print(f"Quantity: {quantity}")
print(f"Price per unit: ${price:.2f}")
print(f"Total price after discount (if applicable): ${total_price:.2f}")

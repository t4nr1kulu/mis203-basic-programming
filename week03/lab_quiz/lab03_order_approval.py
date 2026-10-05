sum = float(input("Enter order amount: "))
stock = int(input("Enter available stock: "))
quantity = int(input("Enter requested quantity: "))
member = input("Are you a member? (yes/no): ")

if quantity <= 0:
    print("Invalid quantity. Order rejected.")
elif stock < quantity:
    print("Insufficient stock. Order rejected.")
elif member == "yes" and sum >= 500:
    final_price = sum * 0.9
    print(f"Order approved with a 10% discount! Final price: {final_price} TRY")
else:
    print(f"Order approved. Final price: {sum} TRY")

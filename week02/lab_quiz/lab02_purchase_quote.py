item1 = input("Item: ")
quantity1 = int(input("Quantity: "))
unit_price1= float(input("Unit price:"))
item2 = input("Item: ")
quantity2 = int(input("Quantity: "))
unit_price2 = float(input("Unit price:"))
delivery_fee = float(input("delivery:"))
tax = int(input("Tax:"))

sub_total = (unit_price1*quantity1) + (unit_price2*quantity2)
tax_percentage = sub_total*(tax/100)
final_total = sub_total+tax_percentage+delivery_fee
print(f"{final_total:.2f}TRY")


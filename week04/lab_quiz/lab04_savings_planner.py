while True:
    start_balance = float(input("Enter starting balance: "))
    deposit = float(input("Enter monthly deposit: "))
    interest_rate = float(input("Enter monthly interest rate (%): "))
    goal = float(input("Enter savings goal: "))
    
    if start_balance < 0 or interest_rate < 0:
        print("Error: Starting balance and interest rate cannot be negative. Try again.")
        continue
    if deposit <= 0 or goal <= 0:
        print("Error: Deposit and goal must be positive. Try again.")
        continue
    
    break

current_balance = start_balance
total_interest = 0.0
months = 0

if current_balance >= goal:
    print("\nGoal already met with starting balance! No saving needed.")
else:
    print("\nMonth | Interest Earned | New Balance")
    print("-" * 37)
    
    while months < 60:
        months += 1
        
        interest = current_balance * (interest_rate / 100)
        current_balance += interest
        current_balance += deposit
        
        total_interest += interest
        
        print(f"{months:<5} | {interest:<15.2f} | {current_balance:.2f}")
        
        if current_balance >= goal:
            break

print("\n--- Summary ---")
if current_balance >= goal:
    print(f"Goal reached in {months} months.")
else:
    print("Goal not reached after 60 months.")

print(f"Final balance: {current_balance:.2f}")
print(f"Total interest earned: {total_interest:.2f}")
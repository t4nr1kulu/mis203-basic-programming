ticket_sold=0
total_revenue=0
free_tickets=0

while True:
  name=input("Customer name (or q to quit): ")
  if name.lower()=="q":
    break
    
  age=input("Age :")
  if age.lower()=="q":
    break
  age_int=int(age)
  if age_int<0 or age_int>120:
    print("İnvalid age!!!")
    continue
    
  day=input("Day (weekday/weekend): ")
  if day.lower()=="q":
    break
  if day.lower()!="weekday"and day.lower()!="weekend":
    print("İnvalid day!!!")
    continue
    
  student=input("Student(yes/no) :")
  if student.lower()=="q":
    break
  if student.lower()!="yes" and student.lower()!="no":
    print("please answer yes or no")
    continue

  if day.lower()=="weekday":
    base_price=200
  else:
    base_price=250

  if age_int<6:
    discount = 100
    ticket_type = "Free"
    free_tickets+=1
    
  elif age_int >= 65:
    discount = 50
    ticket_type = "Senior"
    

  elif age_int >=6 and age_int <=12:
    discount = 40
    ticket_type = "Child"

  elif student.lower() == "yes" and age_int<=25:
    discount = 30
    ticket_type = "Student"

  else:
    discount=0
    ticket_type= "Standart"

  final_price=base_price-(base_price*discount/100)
  print(f"{name}: {final_price:.2f} TRY ({ticket_type})")
  
  ticket_sold += 1
  total_revenue += final_price

if ticket_sold>0:
  aver = total_revenue / ticket_sold
  print(f"Tickets sold :{ticket_sold}")
  print(f"Total revenue:{total_revenue:.2f}TRY")
  print(f"Average price:{aver:.2f}")
  print(f"Free tickets :{free_tickets}")
else:
  print("No tickets sold.")

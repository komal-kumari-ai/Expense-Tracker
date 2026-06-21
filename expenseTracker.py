print("Expense Tracker")
print("Enter any negative or zero number for exit the tracker")
total=0
while True:
    amount=int(input("Enter expense "))
    if amount <=0:
        break
    else:
        total+=amount
    

print("total expenses are",total)


  
  
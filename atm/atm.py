	pin=1150
total=input("enter total amount")
u=input("enter your pin")
if(u==pin):
      withdraw=input("enter amount to be withdraw")
      if(withdraw>total):
          print("your balance is low")
     
      remaning=total-withdraw
      print("reamning balance=",remaning)     


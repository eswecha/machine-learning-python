
totalamount=input("enter the amount")
def atm():
        print("welcome to atm ")
def pin():
        pin=1234
        while(True):
              u=input("enter pin")
              if (u==pin): 
                 print("your pin is correct")
                 break           
        withdraw=input("enter withdraw amount")
        if(withdraw>totalamount):
           print("your balance is low")
           return False                      
        rem=totalamount-withdraw
        print("reamaning balance=",rem)
             
atm()
pin()                     
    
     

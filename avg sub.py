def sai():
    sub1=int(input("Enter marks of the first subject: "))
    sub2=int(input("Enter marks of the second subject: "))
    sub3=int(input("Enter marks of the third subject: "))
    avg=(sub1+sub2+sub3)/3
    if(avg>=75):
          print("grade:A")
    elif(avg>=50):
          print("grade:B")
    elif(avg>=40):
          print("fail")
       

sai()


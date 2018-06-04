
n=int(input("enter number"))
if(n>1):
    for i in  range(2,100):
      if (n%i)==0:
        print(n,"is nor prime")
        print(i,"times",n//i,"is",n)
        break
    else:
        print("is prime number")
else:
        print(" is not prime number")
          

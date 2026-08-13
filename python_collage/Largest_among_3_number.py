a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))
if(a>b):
    if(a>c):
        print(f"{a} is largest number")
elif(b>a):
    if(b>c):
        print(f"{b} is largest number")
else:
    print(f"{c} is largest number")

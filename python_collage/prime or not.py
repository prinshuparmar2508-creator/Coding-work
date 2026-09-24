a = int(input("Enter the number="))
for i in range(2,a//2):
    if a%i == 0:
        print(a,"is not prime")
    else:
        print(a,"is prime")
def hello():
    print("it worked")
print("hmm")
hello()
def calculate_sum(a,b):
    print(a+b)
print("the sum is:")
sum = calculate_sum(3,1)
print(sum)

a= "bro" #global scope can be used both inside and outside of a function
def display():
    a = "code"
    print(a)
print(a)
display()
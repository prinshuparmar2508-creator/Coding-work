arr=list(range(1, 21))
target = int(input("Enter target you want to find: "))
for j in range(len(arr)-1):
    if arr[j]==target:
        print(target,"found at index",j)
    else:
        print(target,"not found in array 1-20")

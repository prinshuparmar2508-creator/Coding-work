arr = list(range(1, 21))
target = int(input("Enter target you want to find: "))
start = 0
end = len(arr) - 1
found = False

while start <= end:
    middle = (start + end) // 2
    if arr[middle] == target:
        print(f"{target} found at index {middle}")
        found = True
        break
    elif arr[middle] > target:
        end = middle - 1
    else:
        start = middle + 1

if not found:
    print(f"{target} not found in arr 1-20")
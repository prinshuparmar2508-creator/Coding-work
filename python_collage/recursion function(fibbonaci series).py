def fibbo(n,a=0,b=1):
    if n == 0:
        return
    print(a, end=" ")
    fibbo(n-1, b, a+b)

fibbo(4)

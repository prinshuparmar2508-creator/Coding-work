def right_triangle(a, b, c):
    if (a*a)==(b*b)+(c*c) or (b*b)==(a*a)+(c*c) or (c*c)==(b*b)+(a*a):
        return "It is a right angle triangle"
    else:
        return "It is not a right angle triangle"


print(right_triangle(7,8,10))
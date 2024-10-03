import random
a = random.randint(1,101)
b = int(input('nhap so'))
c =0
d =100
while b!=a:
    if d>b>a:
        d =b
        

    elif c<b<a:
        c =b
    print(f'so nam trong khoang {c} den {d}')
    b = int(input('nhap so'))
    if b == a :
        print(f'so can tim la {b}')
        break

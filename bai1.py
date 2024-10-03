a,b,c= map(int, input('a,b,c =').split())
# c = int(input())
# print('max = ')
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print (b)
else :
    print(c)
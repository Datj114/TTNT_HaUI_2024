a= int(input('a='))
def checksnt(a):
    if a<=2:
        return False
    for i in range (2,int(a**0.5)+1):
        if a%i==0:
            
            return False
    return True

print(checksnt(a))
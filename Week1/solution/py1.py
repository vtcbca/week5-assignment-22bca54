#WRITE THE PYHON SCREEP ENTER ANY NUMBER AND CHECK IT IS PRIME OR NOT
n=int(input('enter number ::'))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print(f'(n) is a prime number')
else:
    print(f'(n) is not a prime number')

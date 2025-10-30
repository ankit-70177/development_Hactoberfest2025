l=int(input())
r=int(input())

for i in range(l,r+1):
    num=i
    total=0
    nod=len(str(i))
    while num>0:
        ld=num%10
        total+=ld**nod
        num//=10
    if total==i:
        print(total,end=" ")

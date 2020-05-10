lst1=list()
lst2=list()
n=input('enter the no. of elements')
i=0
nc=int(n)
while i!=nc:
    inp=int(input())
    lst1.append(inp)
    i=i+1
for i in lst1:
    if i>=0:
        lst2.append(i)
print(lst2)

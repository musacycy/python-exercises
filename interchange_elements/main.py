l=list=[12,35,9,56,24]
s=len(list)

t=tuple(l)
print(t)

l[0]=t[4]
l[s-1]=t[0]
print(l)

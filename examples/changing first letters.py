a=str(input('unesi prvu rijec: '))
b=str(input('unesi drugu rijec: '))

da=len(a)
pa=a[0]

db=len(b)
pb=b[0]

c=""
c=pb

for i in range(1, da):
  c+=a[i]
c=c+" "+pa
for i in range(1, db):
  c+=b[i]

print(c)

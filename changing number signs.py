a = int(input())
b = int(input())

if(a > 0 and b < 0):
  a = a * (-1)
  b = b * (-1)
elif(b > 0 and a < 0):
  a = a * (-1)
  b = b * (-1)

print("a je: {}, b je: {}".format(a, b))
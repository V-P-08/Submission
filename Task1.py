def factorial(a):
  if a<2:
    return 1
  else :
    return (a*factorial(a-1))

s = factorial(5)
print(s)

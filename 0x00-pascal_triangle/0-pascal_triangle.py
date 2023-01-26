from math import factorial
def pascal_triangle(n):
  """
    returns pascal triagle for a given number n
  """
  li=[]
  for i in range(n):
      a=[]
      for j in range(i+1):
          a.append(factorial(i)//(factorial(j)*factorial(i-j)))
      li.append(a)
  return li
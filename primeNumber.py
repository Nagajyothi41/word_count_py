n=int(input())
for number in range(2, n+1):
  factors = 0
  for i in range(2, number):
    if (number % i) == 0:
      factors = factors + 1
  if factors == 0:
    print(number)


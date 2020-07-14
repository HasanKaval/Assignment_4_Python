number = int(input("Please enter a number  : "))
counter = 0
for i in range(1, number + 1):
  if number%i == 0:
    counter +=1
if counter > 2 or number == 0 or number == 1:
  print(number, "is not a prime number")
else:
  print(number, "is a prime number")
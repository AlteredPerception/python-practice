# The following program will take n as an input to a range (1, n + 1).
# If i % 3 == 0 and i % 5 == 0 print("FizzBuzz")
# if i % 3 == 0 print("Fizz")
# if i % 5 == 0 print("Buzz")
# else print(str(i))

def FizzBuzz(n):
  # This is the range.
  # n = the number to stop at + 1.
  for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(str(i))

if __name__ == '__main__':
  FizzBuzz(20)

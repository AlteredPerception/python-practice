# FizzBuzz programming problem
# using hashing.

def FizzBuzz(n):
  res = []

  # Dictionary to store all FizzBuzz mappings
  mp = {3: "Fizz", 5: "Buzz"}
  divisors = [3, 5]

  for i in range(1, n + 1):
    s = ""

    for d in divisors:
      if i % d == 0:
        s += mp[d]

    if not s:
      s += str(i)

    res.append(s)

  return res


    

if __name__ == '__main__':
  n = 20
  res = FizzBuzz(n)
  
  for s in res:
    print(s, end=" ")

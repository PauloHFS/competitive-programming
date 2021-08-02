#This code is run above the time limit (TLE)

n = int(input())
bills = 0

while n >= 100:
    n -= 100
    bills += 1

while n >= 20:
    n -= 20
    bills += 1

while n >= 10:
    n -= 10
    bills += 1

while n >= 5:
    n -= 5
    bills += 1

while n >= 1:
    n -= 1
    bills += 1

print(bills)




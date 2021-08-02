l = int(input())
n = 0

for i in range(1, l):
    if ((l - i) % i) == 0:
        n += 1

print(n)
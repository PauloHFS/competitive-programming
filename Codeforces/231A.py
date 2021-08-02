n = int(input())

count = 0
for i in range(n):
    x = 0
    for num in input().split():
        x += int(num)
    if x >= 2:
        count += 1

print(count)
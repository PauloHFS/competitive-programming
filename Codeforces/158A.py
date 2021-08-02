n, k = input().split()
scores = [int(i) for i in input().split()]
n, k = int(n), int(k)

kScore = scores[k-1]

count = 0
for i in range(n):
    if scores[i] > 0:
        if scores[i] >= kScore:
            count += 1

print(count)
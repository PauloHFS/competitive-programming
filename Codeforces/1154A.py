numbers = input().split()
abc = []

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

maior = numbers[0]
for i in range(len(numbers)):
    if maior < numbers[i]:
        maior = numbers[i]

for i in range(len(numbers)):
    if numbers[i] != maior:
        abc.append(numbers[i])

abc[0] = maior - abc[0]
abc[1] = abc[1] - abc[0]
abc[2] = abc[2] - abc[0]

for i in abc:
    print(i, end=" ")

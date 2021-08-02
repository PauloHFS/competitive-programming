a, b = input().split()
a, b = int(a), int(b)

ano = 0

while a <= b:
    a = a * 3
    b = b * 2
    ano = ano + 1 

print(ano)
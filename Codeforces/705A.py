layers = int(input())
feeling = ""

for i in range(1, layers + 1):
    if i == 1:
        if i == layers:
            feeling += "I hate it"
        else:
            feeling += "I hate that"
    elif i == layers:
        if i % 2 == 0:
            feeling += " I love it"
        else:
            feeling += " I hate it"
    else:
        if i % 2 == 0:
            feeling += " I love that"
        else:
            feeling += " I hate that"

print(feeling)
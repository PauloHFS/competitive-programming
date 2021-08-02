n = int(input())
thinks = input().split()
isHard = False

for i in thinks:
    if i == "1":
        isHard = True
        break

if isHard:
    print("HARD")
else:
    print("EASY")
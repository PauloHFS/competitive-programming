def isIn(card1, card2):
    for i in range(2):
        if card1[i] == card2[i]:
            return True
    return False

cardDesk = input()
cardHand = input().split()
isPossible = "NO"

for i in range(len(cardHand)):
    if isIn(cardDesk, cardHand[i]):
        isPossible = "YES"
        break

print(isPossible)

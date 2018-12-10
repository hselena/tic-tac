deck = [x for x in range(52)]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
"10", "Jack", "Queen", "King"]
money = 100
import random
X = "X"
while X == "X":
    random.shuffle(deck)
    for i in range(3):
        suit = suits[deck[i] // 13]
        rank = ranks[deck[i] % 13]
        print("Your card", deck[i], "is", rank, "of", suit)
        value = str(int(deck[i] % 13) + 1)
        if i == 0:
            numba = int(value)
        elif i == 1:
            numbb = int(value)
        elif i == 2:
            numbc = int(value)
    Total = numba + numbb + numbc
    if Total > 38:
        print("You won $100!")
        money += 100

    elif Total > 30:
        print("You won $10")
        money += 10

    elif Total > 25:
        print("You won $2")
        money += 2

    else:
        money -= 5
        print("You lost a total of $5")
    print("The total of your three cards is",Total,".","Your balance is $",money,".")
    Y = input("Do you want to play agian? if so select (y/n): ")

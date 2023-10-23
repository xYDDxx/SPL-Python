import random

randomNumber = random.randint(0, 100)

print("Die Zufallszahl ist:", randomNumber)

if randomNumber < 20:
    print("Mini")
elif 20 <= randomNumber <= 50:
    print("Medium")
else:
    print("Large")

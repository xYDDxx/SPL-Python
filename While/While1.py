import random

summe = 0

while True:
    zufallszahl = random.randint(10, 30)
    print("Zufallszahl:", zufallszahl)
    if zufallszahl == 15 or zufallszahl == 25:
        break
    summe += zufallszahl

print("Die Summe der vorherigen Zufallszahlen ist:", summe)

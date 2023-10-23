import random

def addiere_zwei_zahlen(zahl1, zahl2):
    ergebnis = zahl1 + zahl2
    return ergebnis

def zufallszahl_zwischen_100_und_200():
    return random.randint(100, 200)

def zufallswort_aus_array(wort_array):
    return random.choice(wort_array)

ergebnis = addiere_zwei_zahlen(5, 10)
print("Ergebnis der Addition: ", ergebnis)

zufallszah = zufallszahl_zwischen_100_und_200()
print("Zufallszahl: ", zufallszah)

wort_array = ["Apfel", "Banane", "Kirsche", "Orange", "Erdbeere"]
zufallswort = zufallswort_aus_array(wort_array)
print("Zufallswort: ", zufallswort)

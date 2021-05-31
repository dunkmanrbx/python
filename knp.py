# Naimportuj modul random
import random

# Vytvort list moznosti
moznosti = ["Kamen", "Nuzky", "Papir"]


# Vytvort promennou hrac
hrac = input("Zadej jméno hráče: ")

# Vytvort promennou pocitac
pocitac = random.choice(moznosti)

# Vytiskni volbu cloveka a pocitace
volba = input("Co chceš udělat (Kamen, Nuzky, Papir): ")

# Vytvor podminku, zda hrac zvolil neplatnou volbu
if volba != "Kamen" and volba !="Nuzky" and volba != "Papir":
    print("Toto není ve výběru")
    exit()

print("Počítač dal:", pocitac)

# Pokud je volba v poradku, muzeme provest zbytek programu
if volba == "Kamen" and pocitac == "Nuzky":
    print(hrac, " vyhral")
elif volba == "Papir" and pocitac == "Kamen":
    print(hrac, " vyhral")
elif volba == "Nuzky" and pocitac == "Papir":
    print(hrac, " výhral")
elif volba == pocitac:
    print(hrac, " Remízoval")
else:
    print(hrac, " Prohrál")
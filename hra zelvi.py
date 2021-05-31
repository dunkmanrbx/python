import turtle 
import random

obrazovka = turtle.getscreen()

hrac1 = turtle.Turtle()
hrac1.shape("turtle")
hrac1.color("green")
hrac1.penup()
hrac1.goto(300, 60)
hrac1.pendown()
hrac1.circle(40)
hrac1.penup()
hrac1.goto(-200,100)

hrac2 = hrac1.clone()
hrac2.color("blue")
hrac2.penup()
hrac2.goto(300, -140)
hrac2.pendown()
hrac2.circle(40)
hrac2.penup()
hrac2.goto(-200, -100)

for i in range(20):
    if hrac1.pos() >= (300,100):
            print("Hrac 1 vyhrava!")
            break
    elif hrac2.pos() >= (300,-100):
            print("Hrac 2 vyhrava!")
            break
    else:
            hraje_hrac1 = input("Stiskni 'Enter', abys hodil kostkou ")
            kostka = random.randint(1,6)
            print("Kostka: ")
            print(kostka)
            print("Počet kroků bude: ")
            print(20*kostka)
            hrac1.fd(20*kostka)
            hraje_hrac2 = input("Stiskni 'Enter', abys hodil kostkou ")
            kostka = random.randint(1,6)
            print("Kostka: ")
            print(kostka)
            print("Počet kroků bude: ")
            print(20*kostka)
            hrac2.fd(20*kostka)



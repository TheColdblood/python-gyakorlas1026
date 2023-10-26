import math


def elso():
    szam = 0
    while szam < 150:
        print(szam, end=";")
        szam += 2
    print("150")

def masodik():
    szam = 0
    beker = 0
    osszeg = 0
    while szam < 10:
        beker = int(input("Kérem adjon meg 10 egész számot."))
        if beker % 3 == 0:
            osszeg += 1
        szam += 1
    print(osszeg)

def harmadik():
    bekertSzam = 1
    while bekertSzam % 10 != 0:
        bekertSzam = int(input("Kérem adjon meg egész számokat."))
    print(bekertSzam)

def negyedik():
    szam = int(input("Kérem adjon meg egész számokat."))
    while not((((szam >= 10) and (szam <= 99)) or ((szam >= -99) and (szam <= -10))) and (szam % 2 == 0)):
        szam = int(input("Kérem adjon meg egész számokat."))

def otodik():
    szam = int(input("Kérem adjon meg egész számokat."))
    while not(szam <= 0) and (szam % 2 == 0):
        szam = int(input("Kérem adjon meg egész számokat."))

def hatodik():
    szam = int(input("Kérem adjon meg egész számokat."))
    while not(szam % 3 == 0 or (math.sqrt(szam) == int(math.sqrt(szam)))):
        szam = int(input("Kérem adjon meg egész számokat."))
    print(szam)

def hetedik():
    a = int(input("Kérem adjon meg egy egész számot."))
    b = int(input("Kérem adjon meg egy egész számot."))
    c = int(input("Kérem adjon meg egy egész számot."))
    while not(a + b >= c and b + c >= a and a + c > b):
        print("Nem szerkeszhető meg a háromszög.")
        a = int(input("Kérem adjon meg egy egész számot."))
        b = int(input("Kérem adjon meg egy egész számot."))
        c = int(input("Kérem adjon meg egy egész számot."))
    print("A háromszög megszerkeszthető.")

def nyolcadik():
    szoveg = str(input("Kérem gépeljen be egy szöveget."))
    while len(szoveg) < 3:
        szoveg = str(input("Kérem gépeljen be egy szöveget."))
    print(szoveg.upper())

def kilencedik():
    szoveg = str(input("Kérem gépeljen be egy szöveget."))
    while not (szoveg == szoveg.lower() and len(szoveg) > 4):
        print("Próbálja meg kisbetűkkel! (Minimum 4 betű!)")
        szoveg = str(input("Kérem gépeljen be egy szöveget."))

def tizedik():
    szam = int(input("Kérem adjon meg számokat. (Jelezze 0-val ha nem kíván több számot beírni."))
    while not (szam == 0):
        szam = int(input("Kérem adjon meg számokat. (Jelezze 0-val ha nem kíván több számot beírni."))
import random
import math


class bcolors:
    FIOLET = '\033[95m' #fioletowy
    OKBLUE = '\033[94m' #blue
    OKGREEN = '\033[92m' #green
    WSTECZ_YELLOW = '\033[93m' #yellow
    WPRZOD_RED = '\033[91m' #red
    ENDC = '\033[0m' #koniec formatowania
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# print(bcolors.FIOLET+"test"+bcolors.ENDC)
# print(bcolors.OKBLUE+"test"+bcolors.ENDC)
# print(bcolors.OKGREEN+"test"+bcolors.ENDC)
# print(bcolors.WSTECZ_YELLOW+"test"+bcolors.ENDC)
# print(bcolors.WPRZOD_RED+"test"+bcolors.ENDC)
# print(bcolors.BOLD+"test"+bcolors.ENDC)
# print(bcolors.UNDERLINE+"test"+bcolors.ENDC)


def zapis(p, x, a):
    f.write("[" + str(x) + "]\n")
    f.write("1=" + str(p) + "\n")
    f.write("4=" + str(a) + "\n")
    f.write("5=" + str(a - random.randrange(1, 3) * 2) + "\n\n")


def zapis_pos(p, x, a):
    f.write("[" + str(x) + "]\n")
    f.write("1=" + str(p) + "\n")
    f.write("6=" + str(a) + "\n")
    f.write("8=" + str(a - random.randrange(1, 3) * 2) + "\n\n")

def wybor_zakresu(r):
    global zakres_wprzod_gora
    global zakres_wprzod_dol
    global zakres_wtyl_gora
    global zakres_wtyl_dol
    if r <= 1000:
        zakres_wtyl_dol = 1100
        zakres_wtyl_gora = 1200
        zakres_wprzod_dol = 1100 + r / ile_stanowisk
        zakres_wprzod_gora = 1200 + r / ile_stanowisk
        print(
            "r<=1000 " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(
                zakres_wprzod_gora))
    elif r <= 2000:
        zakres_wtyl_dol = 1100
        zakres_wtyl_gora = 1300
        zakres_wprzod_dol = 1100 + r / ile_stanowisk
        zakres_wprzod_gora = 1300 + r / ile_stanowisk
        print(
            "r<=2000 " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(
                zakres_wprzod_gora))
    elif r <= 3000:
        zakres_wtyl_dol = 1100
        zakres_wtyl_gora = 1400
        zakres_wprzod_dol = 1100 + r / ile_stanowisk
        zakres_wprzod_gora = 1400 + r / ile_stanowisk
        print("r<=3000 " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(zakres_wprzod_gora))
    elif r <= 5000:
        zakres_wtyl_dol = 1100
        zakres_wtyl_gora = 1500
        zakres_wprzod_dol = 1100 + r / ile_stanowisk
        zakres_wprzod_gora = 1500 + r / ile_stanowisk
        print(
            "r<=5000 " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(
                zakres_wprzod_gora))
    elif r <= 8000:
        zakres_wtyl_dol = 1100
        zakres_wtyl_gora = 1600
        zakres_wprzod_dol = 1100 + r / ile_stanowisk
        zakres_wprzod_gora = 1600 + r / ile_stanowisk
        print(
            "r<=8000 " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(
                zakres_wprzod_gora))
    elif r <= 11000:
        zakres_wtyl_dol = 1100
        zakres_wtyl_gora = 1700
        zakres_wprzod_dol = 1100 + r / ile_stanowisk
        zakres_wprzod_gora = 1700 + r / ile_stanowisk
        print(
            "r<=11000 " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(
                zakres_wprzod_gora))
    else:
        zakres_wtyl_dol = 1100
        zakres_wtyl_gora = 1800
        zakres_wprzod_dol = 1100 + r / ile_stanowisk
        zakres_wprzod_gora = 1800 + r / ile_stanowisk
        print("r = " + str(r) + " " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(
            zakres_wprzod_dol) + " " + str(zakres_wprzod_gora))


# nazwa_pliku = input("Podaj nazwę pliku do jakiego chcesz zapisać (np. niw1.niw): ")
# print("Podałeś nazwę pliku: " + nazwa_pliku)

nazwa_pliku = r"F:\niw1.niw"
f = open(nazwa_pliku, "w")
f.write("[Niwelacja]\n")
f.write("Ver=2\n")
f.write("Drugi=0\n")
f.write("jednostki=0\n\n")

# reper1 = input("Podaj reper nr 1: ")
# wys_reper1 = int(input("Podaj wysokość reperu nr 1: "))
#
# reper2 = input("Podaj reper nr 2: ")
# wys_reper2 = int(input("Podaj wysokość reperu nr 2: "))
#
# ile_na_osi = int(input("Podaj ilość stanowisk na osi: "))
# wys_doc = int(input("Podaj wysokość stanowiska na osi: "))

reper1 = 5020
wys_reper1 = 196289
reper2 = 5019
wys_reper2 = 198658
ile_na_osi = 4
wys_doc = 199256
wys_biezaca = int(wys_reper1)
print(wys_biezaca)
if ile_na_osi == 1:
    wys_doc2 = wys_reper2
ile_stanowisk = int(input("Podaj ilość stanowisk żeby dojść do stanowiska na osi: "))
r = int(math.fabs(wys_biezaca - wys_doc))

wybor_zakresu(r)

# zakres_wtyl_dol = 500
# zakres_wtyl_gora = 900
# zakres_wprzod_dol = 900
# zakres_wprzod_gora = 1300

if wys_reper1 > wys_doc:
    b = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
    a = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
else:
    a = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
    b = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
# f.write("[1]\n")
# f.write("1=" + str(reper1) + "rp\n")
# f.write("4=" + str(a) + "\n")
# f.write("5=" + str(a - random.randrange(1, 3) * 2) + "\n\n")
zapis(str(reper1) + "rp", 1, a)
wys_biezaca += a
print(bcolors.WSTECZ_YELLOW + "\ta " + str(a) + bcolors.ENDC)
# print(bcolors.WSTECZ_YELLOW + str(wys_biezaca) + " a " + str(a) + bcolors.ENDC)

# f.write("[2]\n")
# # f.write("1=\n")
# # f.write("4=" + str(b) + "\n")
# # f.write("5=" + str(b - random.randrange(1, 3) * 2) + "\n\n")
zapis("", 2, b)
wys_biezaca -= b
print(bcolors.WPRZOD_RED + str(wys_biezaca) + " b " + str(b) + bcolors.ENDC)
ile_stanowisk -= 1
start = 3
step = 2
# for x in range(start, finish, step):
while ile_stanowisk > 0 and 1000000 > wys_biezaca > 0:
    if wys_reper1 > wys_doc:
        b = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
        a = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
    else:
        a = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
        b = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
    # f.write("[" + str(x) + "]\n")
    # f.write("1=\n")
    # f.write("4=" + str(a) + "\n")
    # f.write("5=" + str(a - random.randrange(1, 3) * 2) + "\n\n")
    # r = int(math.fabs(int(wys_biezaca) - int(wys_doc)))
    #if (wys_reper1 > wys_doc and int(wys_doc) >= int(wys_biezaca) + zakres_wtyl_gora) or (wys_reper1 <= wys_doc and int(wys_biezaca) + zakres_wprzod_gora >= int(wys_doc)):
    if (ile_stanowisk == 1 and zakres_wtyl_dol <= int(math.fabs(int(wys_biezaca) - int(wys_doc))) <= zakres_wtyl_gora) or (0 <int(int(wys_doc) - int(wys_biezaca)) <= int(zakres_wtyl_dol)): #and wys_doc <= wys_reper1) or (math.fabs(int((int(wys_biezaca) - int(wys_doc)))) <= int(zakres_wtyl_dol) and wys_reper1 < wys_doc):
        r = int(math.fabs(int(wys_biezaca) - int(wys_doc)))
        zapis("", start, r)
        start += 1
        wys_biezaca += r
        print(bcolors.FIOLET + str(wys_biezaca) + " r " + str(r) + bcolors.ENDC)
        if wys_biezaca == wys_doc:
            print("OK")
        else:
            print(str(wys_biezaca) + " " + str(wys_doc) + " NIE OK")
        zapis("", start, b)
        start += 1
        wys_biezaca -= int(b)
        print(bcolors.WPRZOD_RED + str(wys_biezaca) + " b " + str(b) + bcolors.ENDC)
        break
    elif ile_stanowisk == 1:
        ile_stanowisk += 1
    zapis("", start, a)
    start += 1
    wys_biezaca += int(a)
    print(bcolors.WSTECZ_YELLOW + "\ta " + str(a) + bcolors.ENDC)
    # print(bcolors.WSTECZ_YELLOW + str(wys_biezaca) + " a " + str(a) + bcolors.ENDC)    zapis("", start, b)
    zapis("", start, b)
    start += 1
    wys_doc_real = wys_biezaca
    wys_biezaca -= int(b)
    print(bcolors.WPRZOD_RED + str(wys_biezaca) + " b " + str(b) + bcolors.ENDC)
    ile_stanowisk -= 1

for c in range(ile_na_osi):
    ile_posrednich = input("Podaj liczbę punktów pośrednich (stanowisko na osi nr"+str(c+1)+"): ")
    # ile_posrednich = 0
    for x in range(int(ile_posrednich)):
        posredni = input("Podaj nazwę punktu pośredniego nr " + str(x + 1) + ": ")
        wys_posredni = input("Podaj wysokość punktu pośredniego nr " + str(x + 1) + ": ")
        zapis_pos(posredni, start + x, int(wys_doc) - int(wys_posredni))
    start += int(ile_posrednich)
    if ile_na_osi == 1 or c == ile_na_osi - 1:
        break
    wys_doc2 = int(input("Podaj wysokość stanowiska na osi (nr"+ str(c+2) +"): "))
    ile_stanowisk = int(input("Podaj ilość stanowisk żeby dojść do stanowiska na osi(nr"+ str(c+2) +"): "))
    r = int(math.fabs(wys_biezaca - wys_doc2))

    wybor_zakresu(r)
    # zakres_wtyl_dol = 500
    # zakres_wtyl_gora = 1000
    # zakres_wprzod_dol = 1500
    # zakres_wprzod_gora = 2300
    print(
        "sprawdzanko " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(
            zakres_wprzod_gora) + " wys_biezaca: " + str(wys_biezaca) +  " wys_doc2: " + str(wys_doc2))
    while ile_stanowisk > 0 and 1000000 > wys_biezaca > 0:
        if wys_doc2 < wys_doc:
            b = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
            a = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
            if zakres_wprzod_dol - zakres_wtyl_gora <= wys_biezaca - wys_reper2 <= zakres_wprzod_gora + zakres_wtyl_gora:
                a = random.randrange(int((zakres_wtyl_dol+zakres_wtyl_gora)/4), int(zakres_wtyl_gora / 2)) * 2
                b = random.randrange(int(zakres_wprzod_dol / 2), int((zakres_wprzod_gora+zakres_wprzod_dol) / 4)) * 2
        else:
            a = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
            b = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
            # jak się pojawi błąd dążenia do inf to tutaj dodać analogicznie jak wyżej
        # zapis("", start, a)
        # start += 1
        # wys_biezaca += int(a)
        # print(bcolors.WSTECZ_YELLOW + "\ta " + str(a) + bcolors.ENDC)
        # print(bcolors.WSTECZ_YELLOW + str(wys_biezaca) + " a " + str(a) + bcolors.ENDC)    # r = int(math.fabs(wys_biezaca - int(wys_reper2)))

        # if (wys_reper2 < wys_doc):
        #     print("1111111111111111111111")
        if(zakres_wprzod_dol -100 <= wys_biezaca - wys_doc2 <= zakres_wprzod_gora +100):
            print("2222222222222222222222 "+ str(wys_biezaca - wys_doc2))
        else:
            print("ŹLEE" + str(wys_biezaca - wys_doc2))
        # if (wys_biezaca > wys_reper2):
        #     print("33333333333333333333333")

        print(str(ile_stanowisk) + " " + str(int(wys_doc2) - int(wys_biezaca)))
        if (ile_stanowisk == 1 and zakres_wtyl_dol <= int(math.fabs(int(wys_biezaca) - int(wys_doc2))) <= zakres_wtyl_gora) or (0 < int(int(wys_doc2) - int(wys_biezaca)) <= int(zakres_wtyl_dol)):
            r = int(math.fabs(int(wys_biezaca) - int(wys_doc2)))
            zapis("", start, r)
            start += 1
            wys_biezaca += r
            print(bcolors.FIOLET + str(wys_biezaca) + " r " + str(r) + bcolors.ENDC)
            if wys_biezaca == wys_doc2:
                print("OK "+str(wys_biezaca))
            else:
                print(str(wys_biezaca) + " " + str(wys_doc2) + " NIE OK")
            zapis("", start, b)
            start += 1
            wys_biezaca -= int(b)
            print(bcolors.WPRZOD_RED + str(wys_biezaca) + " b " + str(b) + bcolors.ENDC)
            break
        elif ile_stanowisk == 1:
            ile_stanowisk += 1
        zapis("", start, a)
        start += 1
        wys_biezaca += int(a)
        print(bcolors.WSTECZ_YELLOW + "\ta " + str(a) + bcolors.ENDC)
        # print(bcolors.WSTECZ_YELLOW + str(wys_biezaca) + " a " + str(a) + bcolors.ENDC)    zapis("", start, b)
        zapis("", start, b)
        start += 1
        wys_biezaca -= int(b)
        print(bcolors.WPRZOD_RED + str(wys_biezaca) + " b " + str(b) + bcolors.ENDC)
        ile_stanowisk -= 1
    # input()
    wys_doc = wys_doc2

ile_stanowisk = int(input("Podaj ilość stanowisk żeby dojść do repera nr2: "))
r = int(math.fabs(wys_biezaca - wys_doc))

wybor_zakresu(r)

print(
    "sprawdzanko " + str(zakres_wtyl_dol) + " " + str(zakres_wtyl_gora) + " " + str(zakres_wprzod_dol) + " " + str(
        zakres_wprzod_gora) + " wys_biezaca: " + str(wys_biezaca) + " wys_doc2: " + str(wys_doc2))
# zakres_wtyl_dol = 500
# zakres_wtyl_gora = 1000
# zakres_wprzod_dol = 1500
# zakres_wprzod_gora = 2300

while ile_stanowisk > 0 and 1000000 > wys_biezaca > 0:
    if wys_reper2 < wys_doc:
        b = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
        a = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
        if zakres_wprzod_dol - zakres_wtyl_gora <= wys_biezaca - wys_reper2 <= zakres_wprzod_gora + zakres_wtyl_gora:
            a = random.randrange(int((zakres_wtyl_dol+zakres_wtyl_gora)/4), int(zakres_wtyl_gora / 2)) * 2
            b = random.randrange(int(zakres_wprzod_dol / 2), int((zakres_wprzod_gora+zakres_wprzod_dol) / 4)) * 2

    else:
        a = random.randrange(int(zakres_wprzod_dol / 2), int(zakres_wprzod_gora / 2)) * 2
        b = random.randrange(int(zakres_wtyl_dol / 2), int(zakres_wtyl_gora / 2)) * 2
        # jak się pojawi błąd dążenia do inf to tutaj dodać analogicznie jak wyżej





    zapis("", start, a)
    start += 1
    wys_biezaca += int(a)
    print(bcolors.WSTECZ_YELLOW + "\ta " + str(a) + bcolors.ENDC)
    # print(bcolors.WSTECZ_YELLOW + str(wys_biezaca) + " a " + str(a) + bcolors.ENDC)    # r = int(math.fabs(wys_biezaca - int(wys_reper2)))

    # if (wys_reper2 < wys_doc):
    #     print("1111111111111111111111")
    if(zakres_wprzod_dol -100 <= wys_biezaca - wys_reper2 <= zakres_wprzod_gora +100):
        print("2222222222222222222222 "+ str(wys_biezaca - wys_reper2))
    else:
        print("chuj" + str(wys_biezaca - wys_reper2))
    # if (wys_biezaca > wys_reper2):
    #     print("33333333333333333333333")


    # if ((wys_reper2 < wys_doc and zakres_wprzod_dol-100<= wys_biezaca - wys_reper2 <= zakres_wprzod_gora+100 and wys_biezaca > wys_reper2) or (wys_reper2 >= wys_doc and zakres_wtyl_dol - 100 <= int(wys_biezaca - wys_reper2) <= zakres_wtyl_gora + 100 and wys_biezaca > wys_reper2)):
    if (ile_stanowisk == 1 and zakres_wtyl_dol <= int(math.fabs(int(wys_biezaca) - int(wys_reper2))) <= zakres_wtyl_gora) or (math.fabs(int(wys_reper2) - int(wys_biezaca)) <= int(zakres_wtyl_dol)): #and wys_doc <= wys_reper1) or (math.fabs(int((int(wys_biezaca) - int(wys_doc)))) <= int(zakres_wtyl_dol) and wys_reper1 < wys_doc):
        r = int(math.fabs(wys_biezaca - int(wys_reper2)))
        zapis(str(reper2) + "rp", start, r)
        start += 1
        wys_biezaca -= r
        print(bcolors.FIOLET + str(wys_biezaca) + " r " + str(r) + bcolors.ENDC)
        break
    elif ile_stanowisk == 1:
        ile_stanowisk += 1

    zapis("", start, b)
    start += 1
    wys_biezaca -= int(b)
    print(bcolors.WPRZOD_RED + str(wys_biezaca) + " b " + str(b) + bcolors.ENDC)
    ile_stanowisk -= 1
if wys_biezaca == wys_reper2:
    print("OK")
else:
    print(str(wys_biezaca) + " " + str(wys_reper2) + " NIE OK")
# input()

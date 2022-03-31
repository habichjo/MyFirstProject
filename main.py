# slovnik uzivatelu s hesly
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# analyzovane texty
texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# definice oddelovace pro dalsi pouziti
oddelovac = "-" * 50

# prihlaseni uzivatele
uzivatel = input("Zadej uzivatelske jmeno: ")

# neni-li uzivatel registrovan, ukonci se program
if uzivatel not in uzivatele.keys():
    print("Neregistrovany uzivatel, ukoncuji program.")
    quit()
else:
# zadani hesla
    heslo = input("Zadej heslo: ")

# pokud je zadano spravne heslo, program pokracuje
    if heslo == uzivatele.get(uzivatel):
        print("Vítej v aplikaci.")
# pokud je zadano spatne heslo, ukonci se program
    else:
        print("Špatné heslo, ukončuji program.")
        quit()

# vytisknuti oddelovace pro lepsi orientaci
print(oddelovac)

# nabidne uzivateli moznost vybrat si cislo textu pro analyzu
vybrane_cislo_textu = input("Vyberte, prosím, číslo textu od 1 do 3. ")

# pokud je zadana hodnota numericka...
if vybrane_cislo_textu.isnumeric():
    #...ale neni mezi 1 - 3
    if int(vybrane_cislo_textu) not in range(1, 4):
        # vypise se uzivateli oznameni, ze zadal cislo mimo rozsah a ukonci se program
        print("Vybrali jste číslo mimo povolený rozsah, ukončuji program.")
        quit()
    #je-li cislo v zadanem rozsahu, program pokracuje
    else:
        print(f"Vybrali jste text číslo {vybrane_cislo_textu}")
else:
    # neni-li zadana hodnota ciselna, program skonci
    print("Zadná hodnota není číslo, ukončuji program")
    quit()

# vytisknuti oddelovace pro lepsi orientaci
print(oddelovac)

# do hodnoty vybrany_text se vybere pomoci indexovani (proto - 1) dany text
vybrany_text = texts[int(vybrane_cislo_textu) - 1]

slova_vsechna = []          # seznam vsech slov
slova_prvni_velke = []      # seznam vsech slov zajinacich velkym pismenem
slova_vsechna_velka = []    # seznam vsech slov psanych velkymi pismeny
slova_vsechna_mala = []     # seznam vsech slov psanych malymi pismeny

cisla = []                  # seznam vsech cisel

#pro kazde slovo z vybraneho seznamu
for slovo in vybrany_text.split():
    #...se ocisti o interpunkci
    slovo = slovo.strip(",.")
    #prida slovo do seznamu vsech slov
    slova_vsechna.append(slovo)
    #pokud je slovo cislo, prida do seznamu cisel
    if slovo.isnumeric():
        cisla.append(int(slovo))
    #pokud je slovo s prvni pismenem velky, prida do seznamu techto vyskytu
    if slovo[0].isupper():
        slova_prvni_velke.append(slovo)
    #pokud je slovo se vsemi pismeny velkymi, prida do seznamu techto vyskytu
    if slovo.isupper():
        slova_vsechna_velka.append(slovo)
    #pokud je slovo psane malymi pismeny, prido do seznamu techto vyskytu
    if slovo.islower():
        slova_vsechna_mala.append(slovo)

# pokud jsou v textu nejaka cisla
if len(cisla) > 0:
# definuji promennou soucet a prirazuji ji prozatim hodnotu 0
    soucet = 0

# do promenne soucet postupne nascitam soucet vsech cisel z textu
for cislo in cisla:
    soucet = soucet + cislo

# počet slov
print(f"Počet slov v textu je: {len(slova_vsechna)}")

# počet slov začínajících velkým písmenem,
print(f"Počet slov v textu začínajících velkým písmenem je: {len(slova_prvni_velke)}")

# počet slov psaných velkými písmeny
print(f"Počet slov v textu psaných velkými písmeny je: {len(slova_vsechna_velka)}")

# počet slov psaných malými písmeny
print(f"Počet slov v textu psaných malými písmeny je: {len(slova_vsechna_mala)}")

# počet čísel (ne cifer)
print(f"Pocet čísel v textu je: {len(cisla)}")

# pokud jsou v textu čísla...
if len(cisla) > 0:
    #...zobrazím jejich součet
    print(f"Součet všech čísel (nikoli číslic) v textu je: {soucet}")
else:
    #pokud v textu čísla nejsou, oznámím to uživateli
    print("V zadaném textu nejsou žádná čísla.")

# vytisknuti oddelovace pro lepsi orientaci
print(oddelovac)
# vytisknuti zahlavi
print("LEN |      OCCURENCES      |NR.")
# vytisknuti oddelovace pro lepsi orientaci
print(oddelovac)

# prazdny slovnik pro delky retezců a jejich vyskyty
slova_delka = {}

# projede jednotliva slova v textu
for slovo in slova_vsechna:
    # pokud delka slova jeste neni ve slovniku...
    if len(slovo) not in slova_delka.keys():
        #...prida ji do slovniku a priradi ji vyskyt 1
        slova_delka[len(slovo)] = 1
    else:
        # pokud jiz delka slova existuje, zvysi jeji vyskyt o 1
        slova_delka[len(slovo)] = slova_delka[len(slovo)] + 1

# seradi delky slova od nejnizsi po nejvyssi
for delka in sorted (slova_delka.keys()):
    # do promenne pocet_vyskytu si ulozi hodnotu vyskytu pro danou delku
    pocet_vyskytu = slova_delka[delka]
    # cele to vytiskne
    print(f"{delka:>3} | {'*' * pocet_vyskytu:<20} | {pocet_vyskytu:>2}")


def mijn_functie_2(b, c):
    a = b + c
    d = b - c
    e = b * c
    f = b / c
    return a, d, e, f

# 5
def aanbieding_1(smaak, prijs, korting):
    res = prijs * (1-korting)
    print(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {res} euro.")

aanbieding_1("aardbei", 4, 0.1)

# 6
def inkomsten_totaal(inkomsten):
    totaal = sum(inkomsten)
    print(totaal)

inkomsten_totaal([220, 430, 125, 160, 205, 90, 345])

# 7
def inkomsten_totaal(inkomsten, btw):
    totaal = sum(inkomsten)
    bedrag = btw*totaal
    print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09)

# 8
def laag_en_hoog(mijn_lijst):
    hoog = max(mijn_lijst)
    laag = min(mijn_lijst)
    return hoog, laag

print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

# 9 / 10
def gemiddelde(mijn_lijst2):
    bedrag = sum(mijn_lijst2) / len(mijn_lijst2)
    print(f"De gemiddelde inkomsten deze week zijn {bedrag} euro.")

gemiddelde([220, 430, 125, 160, 205, 90, 345])

# 11
def meervoudig(invoer_lijst):
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

print(meervoudig([10,5,3,2,1,2,9]))

# 12
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    resultaat = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return resultaat

print(combinatie([10,5,3,2,1,2,9]))

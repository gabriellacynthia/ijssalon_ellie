# 2
# print("Opdracht 2")
prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade": 5
}

# 3 
# print("Opdracht 3")
aanbieding = prijzen["aardbei"] *0.8

# 4 
# print ("Opdracht 4")
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}" 
# print(reclame_tekst)

# 5
# print("Opdracht 5")
# print(reclame_tekst.index("€")) # om ongv te weten waar 2.40 eindigt.

reclame_tekst2 = reclame_tekst[:63]
# print(reclame_tekst2)

# 6
# print("Opdracht 6")
reclame_tekst3 = reclame_tekst2.upper()
# print(reclame_tekst3)

# 7 
# print("Opdracht 7")
reclame_tekst4 = reclame_tekst3.split(" ")
# print(reclame_tekst4)

# 8 
# print("Opdracht 8")
# for el in reclame_tekst4:
#    print(el)

# 9
# print("Opdracht 9")
# for el in reclame_tekst4:
#    print(el.lower())

# 10
# print("Opdracht 10")
for el in reclame_tekst4:
    if len(el) >=5:
        print(el.upper())
    else: print(el.lower())

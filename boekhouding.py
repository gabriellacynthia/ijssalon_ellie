from helper import * 
from presentatie import *
import csv

# 2
inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs-totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}

print(inkomsten)

totaal_inkomsten = som(inkomsten)

# 10 
presenteer(inkomsten, totaal_inkomsten)

# 11
with open("boekhouding.csv", "w", newline=  "") as csvfile:
    for key, value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter =";")
        writer.writerow([key,value])
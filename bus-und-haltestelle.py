#bus-und-haltestelle
live = "Herzlich Willkommen zum Bus simulator"
print(live);
zahl1 = int( input("Bitte geben Sie ein wie viele Haltestellen es gibt"))
passagiere = 0
for i in range(zahl1):
    print("Der Bus ist an haltestelle ",i, " angekommen")
    passagiereplus = int(input("Bitte geben Sie an wie viele Passagiere einsteigen"))
    passagiere = passagiere + passagiereplus
    print("Es sind ",passagiere," im Bus")
    

#bus-und-haltestelle
live = "Herzlich Willkommen zum Bus simulator"
print(live);
zahl1 = int( input("Bitte geben Sie ein wie viele Haltestellen es gibt"))
passagiere = 0
for i in range(zahl1):
    print("Der Bus ist an haltestelle ",i, " angekommen")
    passagiereminus = int(input("Bitte geben Sie die zahl an Personen an die Austeigen"))
    passagiereplus = int(input("Bitte geben Sie an wie viele Passagiere einsteigen"))
    if (passagiereplus+passagiere)<60:

        passagiere = passagiere + passagiereplus
        passagiere1 = passagiere - passagiereminus
        print("Es sind ",passagiere1," im Bus")
        if passagiere1 > 60:
            print("Es sind zu viele Passagiere im Bus")
            ab = passagiere1 - 60
            print("Es müssen",ab," Personen austeigen")
    else: print("Achtung Sie überschreiten die Max Anzahl an Personen im Bus")
    

#bus-und-haltestelle
live = "Herzlich Willkommen zum Bus simulator"
print(live);
zahl1 = int( input("Bitte geben Sie ein wie viele Haltestellen es gibt"))
passagiere = 0
for i in range(zahl1):
    print("Der Bus ist an haltestelle ",i, " angekommen")
    passagiereminus = int(input("Bitte geben Sie die zahl an Personen an die Austeigen"))
    if passagiere1 < 60:
        passagiereplus = int(input("Bitte geben Sie an wie viele Passagiere einsteigen"))
    if passagiere1 >= 60:
            print("Es dürfen nur mehr Passagiere austeigen")
    passagiere = passagiere + passagiereplus
    passagiere1 = passagiere - passagiereminus
    if passagiere1<60:
        print("Es sind ",passagiere1," im Bus")
    else:
        print("Es sind zu viele Passagiere im Bus")
        ab = passagiere1 - 60
        print("Es müssen",ab," Personen austeigen")

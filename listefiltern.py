import sys


# Filtert die Temperaturen raus, die nicht zwischen 60 und -60 sind
# und gibt eine neue gefilterte Liste inkl. der Fehlwerte zurück.
def listefiltern(liste):
    filtered = []
    fehlwerte = 0

    for wert in liste:
        if -60 <= wert <= 60:
            filtered.append(wert)
        else:
            fehlwerte += 1
    #ODER:
    #filtered = [wert for wert in liste if -60 <= wert <= 60]
    #fehlwerte = len(liste) - len(filtered)

    return filtered, fehlwerte


# Berechnet die Durchschnittstemperatur der Liste und gibt sie zurück.
def durchschnittfiltern(liste):
    if len(liste) == 0:
        return None

    return sum(liste) / len(liste)


def main():
    liste_tmp = [24,-1,-80,50,-23,22,61,-14,5,34,70,45,-40]
    bereinigt, anzahl_fehler = listefiltern(liste_tmp)
    durchschnitt = durchschnittfiltern(bereinigt)

    if durchschnitt is None:
        print("Die Liste ist leer")
    else:
        print("Bereinigte Liste:", bereinigt)
        print("Fehlwerte:", anzahl_fehler)
        print("Durchschnitt:", durchschnitt, "°C")


if __name__ == '__main__':
    try:
        main()
    except:
        print("Ein Fehler ist aufgetreten!")
        sys.exit(1)
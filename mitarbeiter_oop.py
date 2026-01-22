class Person:
    def __init__(self, name, geschlecht):
        self._name = name
        self._geschlecht = geschlecht

    def get_name(self):
        return self._name

    def get_geschlecht(self):
        return self._geschlecht


class Mitarbeiter(Person):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht)
        self._abteilung = abteilung

    def get_abteilung(self):
        return self._abteilung


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, geschlecht, abteilung):
        super().__init__(name, geschlecht, abteilung)


class Abteilung:
    def __init__(self, name):
        self._name = name
        self._mitarbeiter = []
        self._leiter = None

    def get_name(self):
        return self._name

    def add_mitarbeiter(self, mitarbeiter):
        self._mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter):
        self._leiter = leiter
        self.add_mitarbeiter(leiter)

    def get_leiter(self):
        return self._leiter

    def get_mitarbeiter(self):
        return self._mitarbeiter

    def anzahl_mitarbeiter(self):
        return len(self._mitarbeiter)


class Firma:
    def __init__(self, name):
        self._name = name
        self._abteilungen = []

    def add_abteilung(self, abteilung):
        self._abteilungen.append(abteilung)

    def anzahl_abteilungen(self):
        return len(self._abteilungen)

    def alle_mitarbeiter(self):
        mitarbeiter = []
        for abteilung in self._abteilungen:
            mitarbeiter.extend(abteilung.get_mitarbeiter())
        return mitarbeiter

    def anzahl_mitarbeiter(self):
        return len(self.alle_mitarbeiter())

    def anzahl_abteilungsleiter(self):
        count = 0
        for abteilung in self._abteilungen:
            if abteilung.get_leiter() is not None:
                count += 1
        return count

    def groesste_abteilung(self):
        if len(self._abteilungen) == 0:
            return None

        groesste = self._abteilungen[0]
        for abteilung in self._abteilungen:
            if abteilung.anzahl_mitarbeiter() > groesste.anzahl_mitarbeiter():
                groesste = abteilung
        return groesste

    def geschlechter_prozent(self):
        mitarbeiter = self.alle_mitarbeiter()
        if len(mitarbeiter) == 0:
            return 0, 0

        maenner = 0
        frauen = 0

        for m in mitarbeiter:
            if m.get_geschlecht() == "m":
                maenner += 1
            elif m.get_geschlecht() == "w":
                frauen += 1

        gesamt = len(mitarbeiter)
        return (frauen / gesamt) * 100, (maenner / gesamt) * 100




firma = Firma("HTL GmbH")

it = Abteilung("IT")
verkauf = Abteilung("Verkauf")

firma.add_abteilung(it)
firma.add_abteilung(verkauf)

m1 = Mitarbeiter("Anna", "w", it)
m2 = Mitarbeiter("Enes", "m", it)
m3 = Mitarbeiter("Raphi", "m", verkauf)

leiter_it = Abteilungsleiter("Lucas", "m", it)
leiter_verkauf = Abteilungsleiter("Sarah", "w", verkauf)

it.add_mitarbeiter(m1)
it.add_mitarbeiter(m2)
it.set_leiter(leiter_it)

verkauf.add_mitarbeiter(m3)
verkauf.set_leiter(leiter_verkauf)

# Ausgaben
print("Abteilungen:", firma.anzahl_abteilungen())
print("Mitarbeiter:", firma.anzahl_mitarbeiter())
print("Abteilungsleiter:", firma.anzahl_abteilungsleiter())

groesste = firma.groesste_abteilung()
print("Größte Abteilung:", groesste.get_name())

frauen, maenner = firma.geschlechter_prozent()
print("Frauen:", round(frauen, 2), "%")
print("Männer:", round(maenner, 2), "%")

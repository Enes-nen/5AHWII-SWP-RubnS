
class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def vorstellen(self):
        print(f"Hallo, ich heiße {self.name}.")

    def zeige_alter(self):
        print("Ich bin", self.alter, "Jahre alt.")


class Schueler(Person):
    def lernen(self):
        print(f"{self.name} lernt für einen Test.")
        super().zeige_alter()


class Lehrer(Person):
    def unterrichten(self):
        print(f"{self.name} unterrichtet die Klasse.")
        super().zeige_alter()


def main():
    schueler1 = Schueler("Enes", 20)
    lehrer1 = Lehrer("Herr Rubner", 45)

    schueler1.vorstellen()
    schueler1.lernen()

    print()

    lehrer1.vorstellen()
    lehrer1.unterrichten()

if __name__ == "__main__":
    try:
        main()
    except:
        print("Fehler")
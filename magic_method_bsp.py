class Auto:
    def __init__(self, ps): # Konstruktor
        self.ps = ps

    def __repr__(self): # Technische Ausgabe
        return f"Auto({self.ps} PS)"

    def __add__(self, other): # Addition
        if isinstance(other, Auto):
            return self.ps + other.ps
        elif isinstance(other, (int, float)):
            return self.ps + other
        else:
            raise TypeError("Addition Fehler")

    def __sub__(self, other): # Subtraktion
        if isinstance(other, Auto):
            return self.ps - other.ps
        elif isinstance(other, (int, float)):
            return self.ps - other
        else:
            raise TypeError("Subtraktion Fehler")

    def __mul__(self, other): # Multiplikation
        if isinstance(other, Auto):
            return self.ps * other.ps
        elif isinstance(other, (int, float)):
            return self.ps * other
        else:
            raise TypeError("Multiplikation Fehler")

    def __eq__(self, other): # Gleich (==)
        if isinstance(other, Auto):
            return self.ps == other.ps
        return False

    def __lt__(self, other): # Kleiner als (<)
        if isinstance(other, Auto):
            return self.ps < other.ps
        else:
            raise TypeError("Vergleich '<' Fehler")

    def __gt__(self, other): # Größer als (>)
        if isinstance(other, Auto):
            return self.ps > other.ps
        else:
            raise TypeError("Vergleich '>' Fehler")

if __name__ == "__main__":
    firma = Auto("firma")
    a1 = Auto(50)
    a2 = Auto(60)
    a3 = Auto(50)

    print(f"Auto 1: {a1}")
    print(f"Auto 2: {a2}")

    print(f"Addition (50 + 60): {a1 + a2}")

    print(f"Subtraktion (60 - 50): {a2 - a1}")

    print(f"Multiplikation (50 * 60): {a1 * a2}")

    print(f"Ist a1 == a3? {a1 == a3}")
    print(f"Ist a1 < a2?  {a1 < a2}")
    print(f"Ist a1 > a2?  {a1 > a2}")

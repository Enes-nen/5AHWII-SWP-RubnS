import random

class ListElement:
    """Repräsentiert ein einzelnes Element (Knoten) in der Liste."""

    def __init__(self, obj):
        self.obj = obj
        self.next_elem = None

    def get_obj(self):
        return self.obj


class EinfachVerketteteListe:
    """Die einfach verkettete Liste mit allen Java-Methoden."""

    def __init__(self):
        self.start_elem = ListElement("Kopf")

    def add_last(self, o):
        new_elem = ListElement(o)
        last_elem = self.get_last_elem()
        last_elem.next_elem = new_elem

    def insert_after(self, prev_item, new_item):
        pointer_elem = self.start_elem.next_elem
        # Suchen, bis wir das Element finden oder am Ende sind
        while pointer_elem is not None and pointer_elem.obj != prev_item:
            pointer_elem = pointer_elem.next_elem

        # Wenn gefunden, dazwischen einfügen
        if pointer_elem is not None:
            new_elem = ListElement(new_item)
            next_elem = pointer_elem.next_elem
            pointer_elem.next_elem = new_elem
            new_elem.next_elem = next_elem

    def delete(self, o):
        le = self.start_elem
        # Suchen nach dem Element, dessen NACHFOLGER gelöscht werden soll
        while le.next_elem is not None:
            if le.next_elem.obj == o:
                # Zeiger umbiegen, um das Element auszuketten
                le.next_elem = le.next_elem.next_elem
                break
            le = le.next_elem

    def find(self, o):
        le = self.start_elem
        while le is not None:
            if le.obj == o:
                return True
            le = le.next_elem
        return False

    def get_first_elem(self):
        return self.start_elem

    def get_last_elem(self):
        le = self.start_elem
        while le.next_elem is not None:
            le = le.next_elem
        return le

    def write_list(self):
        le = self.start_elem
        while le is not None:
            print(le.obj)
            le = le.next_elem

    def __len__(self):
        """Erlaubt die Nutzung von len(liste). Zählt ab dem ersten echten Element."""
        count = 0
        current = self.start_elem.next_elem  # Startet nach dem 'Kopf'
        while current is not None:
            count += 1
            current = current.next_elem
        return count

    def __iter__(self):
        """Macht die Liste iterierbar"""
        self._iter_current = self.start_elem.next_elem
        return self

    def __next__(self):
        """Gibt das nächste Element für den Iterator zurück."""
        if self._iter_current is None:
            raise StopIteration

        current_val = self._iter_current.obj
        self._iter_current = self._iter_current.next_elem
        return current_val


if __name__ == "__main__":
    # 1. Test: Ganzahlen Beispiel
    print("Test 1:")
    liste = EinfachVerketteteListe()
    liste.add_last("5")
    liste.add_last("2")
    liste.add_last("1")
    liste.add_last("7")
    liste.add_last("8")
    liste.add_last("9")
    liste.insert_after("7", "neu")
    liste.delete("1")
    liste.write_list()

    print("erstes Element:", liste.get_first_elem().get_obj())
    print("letztes Element:", liste.get_last_elem().get_obj())
    print("ist '1' enthalten?", liste.find("3"))
    print("ist 'neu' enthalten?", liste.find("neu"))

    # 2. Test: Zufallszahlen, Länge und Iterator-Protokoll
    print("\nTest 2:")
    zufalls_liste = EinfachVerketteteListe()

    for _ in range(5):
        zufalls_liste.add_last(random.randint(1, 100))

    print(f"Länge der Datenstruktur: {len(zufalls_liste)}")

    print("Ausgabe aller Elemente:")
    for element in zufalls_liste:
        print(element)
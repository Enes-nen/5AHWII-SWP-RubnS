
# if/else
x = 10

if x > 5:
    print("x ist größer als 5")
else:
    print("x ist 5 oder kleiner")

# For-Schleife über eine Liste
zahlen = [1, 2, 3]
for z in zahlen:
    print("Zahl:", z)

# While-Schleife bis Bedingung erfüllt ist
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# break
for i in range(10):
    if i == 5:
        print("Abbruch bei i =", i)
        break
    print(i)

# pass
def noch_nicht_fertig():
    pass  # Platzhalter, damit der Code lauffähig bleibt

print("Programm läuft trotzdem weiter")

# try/except/finally
try:
    zahl = int("abc")  # Fehler: "abc" kann nicht in eine Zahl umgewandelt werden
except ValueError:
    print("Das war keine gültige Zahl!")
finally:
    print("Ich werde immer ausgeführt!")

# try/except/else/finally
try:
    zahl = int(1.2)  # Fehler: "xxx" kann nicht in eine Zahl umgewandelt werden
except ValueError:
    print("Das war keine gültige Zahl!")
else:
    print("Nicht bekannter Fehler!")
finally:
    print("Ich werde immer ausgeführt!")

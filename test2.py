
# List-Comprehension:
#   Reihenfolge bleibt gleich
#   Duplikate werden nicht entfernt
number = [1, 2, 2, 3, 4, 4, 5]
double = [x * 2 for x in number]
print(double)

tuple = (1, 2, 2, 3, 4, 4, 5)
print(tuple)

# Set-Comprehension:
#   Duplikate werden entfernt
numbers = [2, 1, 2, 3, 5, 4, 4]
doubles = {x * 2 for x in numbers}
print(doubles)

# Set-Comprehension mit if-else:
#   Wenn die Zahl gerade ist → verdoppeln
#   Wenn sie ungerade ist → verdreifachen
numbers2 = [2, 1, 2, 3, 5, 4, 4]
doubles2 = {x * 2 if x % 2 == 0 else x * 3 for x in numbers2}
print(doubles2)

# Dict Comprehension:
#   Schlüssel-Wert-Paar
#   Schlüssel = Wort, Wert = Länge des Wortes
words = ["Apfel", "Banane", "Kirsche"]
word_length = {word: len(word) for word in words}
print(word_length)


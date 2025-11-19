# dict comprehesnion:
# english Alphabet 26 Buchstaben -> dictionary (A1, B2, C3, ...)

letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N'
             ,'O','P','Q','R','S','T','U','V','W','X','Z']

l2 = {letters[i]: i+1 for i in range(len(letters))}
print(l2)

"""""
l = {}
for i in range(len(letters)):
    l[letters[i]] = i + 1

print(l)
"""""
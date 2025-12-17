names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
ages = [23, 17, 34, 15, 29]
scores = [88, 92, 75, 64, 91]

# 1. zip – kombiniere zu (name, age, score)
combined = list(zip(names, ages, scores))
print(combined)

# 2. filter + lambda – Alter ≥ 18 und Score ≥ 80
filtered = list(filter(lambda person: person[1] >= 18 and person[2] >= 80, combined))
print(filtered)

# 3. map + lambda – Umwandlung in Dictionaries
result = list(map(lambda person: {
    "name": person[0],
    "age": person[1],
    "score": person[2]
}, filtered))

print(result)

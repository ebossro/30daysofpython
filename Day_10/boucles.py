# Itérer 0 à 10 en utilisant pour la boucle, faites de même en utilisant la boucle.

i = 0
while i <= 10:
    print(i)
    i += 1

# Iléter 10 à 0 en utilisant pour la boucle, faites de même en utilisant la boucle pendant.

i = 10
while i >= 0:
    print(i)
    i -= 1

# Écrivez une boucle qui fait sept appels à imprimer (), nous obtenons donc sur la sortie le triangle suivant:

i = 0
while i < 7:
    print("*" * (i + 1))
    i += 1

# Utilisez des boucles imbriquées pour créer ce qui suit:

for i in range(6):
    for j in range(13):
        print("# ", end="")
    print() 

# Imprimez le modèle suivant:

for i in range(11):
    print(f"{i} x {i} = {i * i}")

# itérer dans la liste, [«python», «numpy», «pandas», «django», «flask»] en utilisant une boucle pour une boucle et imprimez les éléments.

languages = ["python", "numpy", "pandas", "django", "flask"]
for language in languages:
    print(language)

# Utiliser pour la boucle pour itérer de 0 à 100 et imprimer uniquement les nombres pairs.
for i in range(101):
    if i % 2 == 0:
        print(i)

# Utiliser pour la boucle pour itérer de 0 à 100 et imprimer uniquement les nombres impairs

for i in range(101):
    if i % 2 != 0:
        print(i)

# Exercie 2 

# Utiliser pour la boucle pour itérer de 0 à 100 et imprimer la somme de tous les nombres.
somme = 0
for i in range(101):
    somme += i
print(somme)

# 1. Utilisez pour la boucle pour itérer de 0 à 100 et imprimez la somme de tous les evens et la somme de toutes les chances.

somme_pairs = 0
somme_impairs = 0
for i in range(101):
    if i % 2 == 0:
        somme_pairs += i
    else:
        somme_impairs += i
print(f"La somme des nombres pairs est {somme_pairs}.")
print(f"La somme des nombres impairs est {somme_impairs}.")
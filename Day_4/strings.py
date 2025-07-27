#1. Concaténer la chaine de caractères

print("trente " + "jours " + "de " + "python")

# 2. Concaténer la chaine de caractères

print("codeage " + "pour " + "all")

# 3. Déclarer une variable

societe = "codage pour tous"

# 4. Afficher la variable

print(f'{societe}')

# 5. Afficher la longueur de la chaîne

print(f'{len(societe)}')

# 6. Changer les caractères en majuscules

print(f'{societe.upper()}')

# 7. Changer les caractères en minuscules

print(f'{societe.lower()}')

# 8. Les méthodes

chaine3 = "Coding For All"

print(chaine3.capitalize())

print(chaine3.title())

print(chaine3.swapcase())

# 9. Couper le premier mot
print(chaine3[7:])

# 10. Vérifier si 'Coding' dans chaîne
print("Coding" in chaine3)

# 11. Remplacer codage par Python
print(societe.replace("codage", "Python"))

# 12. Remplacer 'Python for Everyone' par 'Python for All'
chaine4 = "Python for Everyone"
print(chaine4.replace("Everyone", "All"))

# 13. Split
print(societe.split(" "))

# 14. Split par virgule
entreprises = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(entreprises.split(", "))

# 15. Caractère index 0
print(chaine3[0])

# 16. Dernier index
print(chaine3[-1])

# 17. Caractère index 10
print(societe[10])

# 18. Acronyme "Python For Everyone"
mots = "Python For Everyone".split()
acronyme = "".join([mot[0].upper() for mot in mots])
print(acronyme)

# 19. Acronyme "codage pour tous"
mots2 = "codage pour tous".split()
acronyme2 = "".join([mot[0].upper() for mot in mots2])
print(acronyme2)

# 20. Position de 'C'
print(chaine3.index("C"))

# 21. Position de 'F'
print(chaine3.index("F"))

# 22. Dernière occurrence de 'l'
print(chaine3.rfind("l"))

# 23. Première occurrence 'because'
phrase = "You cannot end a sentence with because because because is a conjunction"
print(phrase.find("because"))

# 24. Dernière occurrence 'because'
print(phrase.rindex("because"))

# 25. Slice "because because"
start = phrase.find("because")
end = phrase.rindex("because") + len("because")
print(phrase[start:end])

# 26. Position première 'because'
print(phrase.find("because"))

# 27. Slice "because because"
print(phrase[start:end])

# 28. Commence par "Coding"
print(chaine3.startswith("Coding"))

# 29. Finit par "coding"
print(societe.endswith("coding"))

# 30. Strip espaces
chaine5 = "   Codage pour tous   "
print(chaine5.strip())

# 31. isidentifier()
print("30daysofpython".isidentifier())
print("Thirty_days_of_python".isidentifier())

# 32. Join liste bibliothèques
libs = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print(" # ".join(libs))

# 33. Nouvelle ligne
print("J'apprécie ce défi.\nJe me demande juste quelle est la prochaine étape.")

# 34. Séquence tabulation
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35. Formatage rayon
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} square meters.".format(radius, area))

# 36. Calculs formatés
a, b = 8, 6
print("{} + {} = {}".format(a, b, a + b))
print("{} - {} = {}".format(a, b, a - b))
print("{} * {} = {}".format(a, b, a * b))
print("{} / {} = {:.2f}".format(a, b, a / b))
print("{} % {} = {}".format(a, b, a % b))
print("{} // {} = {}".format(a, b, a // b))
print("{} ** {} = {}".format(a, b, a ** b))

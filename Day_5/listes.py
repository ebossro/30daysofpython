# 1. Déclarer une liste vide
empty_list = []

# 2. Déclarer une liste avec plus de 5 articles
items = ['stylo', 'cahier', 'ordinateur', 'chaise', 'bouteille', 'téléphone']

# 3. Trouver la taille de la liste
print(len(items))

# 4. Premier, élément moyen et dernier élément
print(items[0], items[len(items)//2], items[-1])

# 5. Liste mixtes_data_types
mixed_data_types = ['Emmanuel', 21, 1.75, 'Célibataire', 'Lomé']

# 6. Liste IT_COMPANIES
IT_COMPANIES = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Afficher la liste
print(IT_COMPANIES)

# 8. Nombre d’entreprises
print(len(IT_COMPANIES))

# 9. Première, moyenne et dernière société
print(IT_COMPANIES[0], IT_COMPANIES[len(IT_COMPANIES)//2], IT_COMPANIES[-1])

# 10. Modifier une société
IT_COMPANIES[2] = 'Microsoft Corp'
print(IT_COMPANIES)

# 11. Ajouter une société
IT_COMPANIES.append('Twitter')
print(IT_COMPANIES)

# 12. Insérer une société au milieu
IT_COMPANIES.insert(len(IT_COMPANIES)//2, 'Netflix')
print(IT_COMPANIES)

# 13. Changer un nom
IT_COMPANIES[1] = IT_COMPANIES[1].upper()
print(IT_COMPANIES)

# # 14. Joindre les sociétés
IT_COMPANIES_JOIN = "#; ".join(IT_COMPANIES)
print(IT_COMPANIES_JOIN)

# 15. Vérifier si une entreprise existe
print('Apple' in IT_COMPANIES)

# 16. Trier la liste
IT_COMPANIES.sort()
print(IT_COMPANIES)

# 17. Inverser la liste
IT_COMPANIES.reverse()
print(IT_COMPANIES)

# 18. Éliminer les 3 sociétés
IT_COMPANIES.pop(2)
print(IT_COMPANIES)

# 19. Éliminer les 3 sociétés
IT_COMPANIES.pop(2)
print(IT_COMPANIES)

# 20. Trancher les sociétés du milieu
mid = len(IT_COMPANIES) // 2
print(IT_COMPANIES[mid-1:mid+1])

# 21. Supprimer la première société
IT_COMPANIES.pop(0)
print(IT_COMPANIES)

# 22. Supprimer les sociétés du milieu

mid = len(IT_COMPANIES) // 2
del IT_COMPANIES[mid-1:mid+1]
print(IT_COMPANIES)

# 23. Supprimer la dernière société

IT_COMPANIES.pop()
print(IT_COMPANIES)

# 24. Supprimer toute la société

IT_COMPANIES.clear()
print(IT_COMPANIES)

# 25. Supprimer la liste

del IT_COMPANIES

# 26. Joindre front_end et back_end
front_end = ['html', 'css', 'js', 'react', 'redux']
back_end = ['node', 'express', 'mongodb']
full_stack = front_end + back_end
print(full_stack)

# 27. Insérer Python et SQL après Redux
full_stack.insert(full_stack.index('redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)

# Exercices 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Trier et trouver min et max
ages.sort()
min_age, max_age = ages[0], ages[-1]
print(min_age, max_age)

# Ajouter à nouveau min et max
ages.append(min_age)
ages.append(max_age)

# Trouver la médiane
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
print(median)

# Moyenne
average = sum(ages) / len(ages)
print(average)

# Range
age_range = max_age - min_age
print(age_range)

# Moyenne abs (écart avec moyenne)
print(abs(min_age - average), abs(max_age - average))

# Liste des pays
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = len(countries) // 2
print(countries[mid])

# Diviser la liste en deux
if len(countries) % 2 == 0:
    first_half = countries[:mid]
    second_half = countries[mid:]
else:
    first_half = countries[:mid + 1]
    second_half = countries[mid + 1:]
print(first_half, second_half)

# Décomposer trois premiers et pays scandinaves
first_three, scandic_countries = countries[:3], countries[3:]
print(first_three, scandic_countries)

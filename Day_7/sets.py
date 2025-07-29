# 1. la longueur de l'ensemble IT_COMPANIES

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26} 
b = {19, 22, 20, 25, 26, 24, 28, 27} 
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

# 2. Insérer plusieurs sociétés informatiques

it_companies.update(['Twitter', 'Tesla'])
print(it_companies)

# 4. Supprimer l'une des sociétés de l'ensemble IT_COMPANIES

it_companies.remove('Oracle')
print(it_companies)

# 5. Quelle est la différence entre supprimer et rejeter

# Supprimer lève une erreur si l'élément n'existe pas, tandis que rejeter ne le fait pas.

# Exercice 2

# 1. Rejoignez A et B

a.update(b)
print(a)

# 2. Trouvez une intersection B
print(a.intersection(b))

# 3. Est un sous-ensemble de B

print(a.issubset(b))

# 4. Les ensembles disjoints A et B

print(a.isdisjoint(b))

# 5. rejoindre A avec B et B avec A
a.update(b)
print(a)
b.update(a)
print(b)

# 6. Quelle est la différence symétrique entre A et B
print(a.symmetric_difference(b))

# 7. Supprimer les ensembles complètement

del a
del b

# Exercice 3

# 1. Convertissez les âges en un ensemble et comparez la longueur de la liste et de l'ensemble, qui l'un est plus grand

age_set = set(age)
print(len(age))
print(len(age_set))

# 2. Expliquez la différence entre les types de données suivants: chaîne, liste, tuple et ensemble

# Chaîne est une séquence de caractères immuable.
# Liste est une collection ordonnée et modifiable d'éléments.
# Tuple est une collection ordonnée et immuable d'éléments.
# Ensemble est une collection non ordonnée d'éléments uniques.

# 3. I am a teacher and I love to inspire and teach people. Combien de mots uniques ont été utilisés dans la phrase? Utilisez les méthodes Split et définissez pour obtenir les mots uniques.

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print(len(unique_words))
# --- Niveau 1 ---

# 1. Créez un tuple vide
empty_tuple = ()

# 2. Tuple avec noms des sœurs et frères
sisters = ('Aline', 'Sophie')
brothers = ('Marc', 'Paul')

# 3. Joindre tuples frères et sœurs
siblings = sisters + brothers
print(siblings)

# 4. Combien de frères et sœurs ?
print(len(siblings))

# 5. Ajouter parents
family_members = siblings + ('Jean', 'Marie')
print(family_members)

# --- Niveau 2 ---

# 1. Déballer frères et sœurs + parents
sister1, sister2, brother1, brother2, father, mother = family_members
print(sister1, sister2, brother1, brother2, father, mother)

# 2. Créer fruits, légumes, produits animaux et joindre
fruits = ('pomme', 'banane', 'orange')
vegetables = ('tomate', 'carotte', 'salade')
animal_products = ('lait', 'fromage', 'œufs')

food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Convertir tuple en liste
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4. Couper l’article du milieu ou les articles
mid = len(food_stuff_lt) // 2
print(food_stuff_lt[mid])

# 5. Couper les trois premiers et trois derniers éléments
print(food_stuff_lt[:3], food_stuff_lt[-3:])

# 6. Supprimer le tuple food_stuff_tp
del food_stuff_tp

# 7. Vérifier si un élément existe en tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

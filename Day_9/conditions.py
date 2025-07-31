# 1

age = input('Entrez votre âge: ')
if int(age) >= 18:
    print("Vous êtes assez âgé pour apprendre à conduire.")
else:
    print(f"Il vous manque {18 - int(age)} ans pour apprendre à conduire.")

# 2

age = input("Entrez votre âge : ")

if int(age) >= 25:
    print(f'Vous avez {int(age) - 25} ans de plus que moi.')
else:
    print(f'Vous avez {25 - int(age)} ans de moins que moi.')

# 3

premier_nombre = int(input("Entrez le premier nombre: "))
deuxieme_nombre = int(input("Entrez le deuxième nombre: "))

if premier_nombre > deuxieme_nombre:
    print(f"{premier_nombre} est plus grand que {deuxieme_nombre}.")
elif premier_nombre < deuxieme_nombre:
    print(f"{premier_nombre} est plus petit que {deuxieme_nombre}.")
else:
    print(f"{premier_nombre} est égal à {deuxieme_nombre}.")

# Exercie 2

# 1

score = int(input("Entrez le score de l'élève: "))

if 80 <= score <= 100:
    print("Note: A")
elif 70 <= score < 80:
    print("Note: B")
elif 60 <= score < 70:
    print("Note: C")
elif 50 <= score < 60:
    print("Note: D")
else:
    print("Note: F")

# 2

mois = input("Entrez un mois: ").strip().lower()

if mois in ["septembre", "octobre", "novembre"]:
    print("Saison: Automne")
elif mois in ["décembre", "janvier", "février"]:
    print("Saison: Hiver")
elif mois in ["mars", "avril", "mai"]:
    print("Saison: Printemps")
elif mois in ["juin", "juillet", "août"]:
    print("Saison: Été")
else:
    print("Mois invalide.")

# 3

fruits = ['banana', 'orange', 'mango', 'lemon']

choice = input("Entrez un fruit: ").strip().lower()

if choice in fruits:
    print(f"Ce fruit existe déjà dans la liste.")
else:
    fruits.append(choice)
    print(f"{choice} a été ajouté à la liste des fruits.")
    print("Liste des fruits mise à jour:", fruits)

# Exercicce 3

# 1

person={
    'first name': 'Asabeneh',
    'last name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Compétence du milieu:", skills[middle_index])
    if 'Python' in skills:
        print("La personne a la compétence Python.")
    else:
        print("La personne n'a pas la compétence Python.")

if 'JavaScript' in skills and 'React' in skills:
    print("Titre: Développeur front-end")
elif 'Python' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("Titre: Développeur backend")
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print("Titre: Développeur fullstack")
else:
    print("Titre: Inconnu")

if person['is marred'] and person['country'] == 'Finland':
    print(f"{person['first name']} {person['last name']} vit en {person['country']}. Il est marié.")

# 1. Créez un dictionnaire vide appelé chien

chien = {}

# 2. Ajouter le nom, la couleur, la race, les jambes, l'âge au dictionnaire pour chiens

chien = {'nom': 'Leroy', 'couleur': "Brun", 'race': 'Berger Allemand', 'jambes': 4, 'age': 5}

# 3. Créez un dictionnaire étudiant et ajoutez d'abord_name, last_name, sexe, âge, état matrimonial, compétences, pays, ville et adresse comme clés pour le dictionnaire

etudiant = {
    'first_name': 'Geoffrey',
    'last_name': 'Python',
    'gender': 'M',
    'age': 27,
    'marital_status': 'Célibataire',
    'skills': ['Python'],
    'country': 'Togo',
    'city': 'Lomé',
    'address': 'Agoè'
}

# 4. Obtenez la longueur du dictionnaire étudiant

print(len(etudiant))

# 5. Vérifier le type de "skills"

print(type(etudiant['skills']))

# 6. Modifiez les valeurs de "skills" en ajoutant une ou deux compétences.

etudiant['skills'].append('HTML')
etudiant['skills'].append('Django')

print(etudiant)

# 7. Obtenez les clés du dictionnaire sous forme de liste.

print(etudiant.keys())

# 8. Obtenez les valeurs du dictionnaire sous forme de liste.

print(etudiant.values())

# 9. Changez le dictionnaire en une liste de tuples en utilisant la méthode items().

print(etudiant.items())

# 10. Supprimez un des éléments du dictionnaire.

print(etudiant.pop('marital_status'))

# 11. Supprimez un des dictionnaires.

del etudiant
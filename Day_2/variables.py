#Jour 2: 30 Days of Python Programming

# 1. Vérifier le type de vos variables

prenom = "Emmanuel"

nom = "Bossro"

nom_complet = "Emmanuel Bossro"

pays = "Togo"

age = 30


# 2. Longueur du prénom

print(type(prenom))
print(type(nom))
print(type(nom_complet)) 
print(type(pays))    
print(type(age))    

print(len(prenom))

# 3. Comparer la longueur prénom et nom

print(len(prenom) > len(nom)) 

# 4. Déclarer num_one et num_two

number_one = 5
number_two = 4

# 5. Addition

somme = number_one + number_two
print(somme)


# 6. Soustraction
difference = number_one - number_two
print(difference)

# 7. Multiplication
produit = number_one * number_two
print(produit)

# 8. Division
division = number_one / number_two
print(division)

# 9. Division modulo (reste)
reste = number_two % number_one
print(reste)

# 10. Division entière (floor division)
floor_division = number_one // number_two
print(floor_division)

# 12. Calculs avec le cercle
rayon = 30
pi = 3.1416

# i. Aire
area_of_circle = pi * rayon ** 2
print(area_of_circle)

# ii. Circonférence
circum_of_circle = 2 * pi * rayon
print(circum_of_circle)

# iii. Rayon en entrée utilisateur
rayon_user = float(input("Entrez le rayon : "))
area_user = pi * rayon_user ** 2
print(area_user)

# 13. Entrée utilisateur pour prénom, nom, pays, âge
prenom_user = input("Votre prénom : ")
nom_user = input("Votre nom : ")
pays_user = input("Votre pays : ")
age_user = input("Votre âge : ")

# 14. Aide sur les mots-clés Python
help("keywords")
# 1. Déclarer âge
age = 21

# 2. Déclarer taille
taille = 1.75

# 3. Déclarer un nombre complexe
nombre_complexe = 4 + 5j

# 4. Aire du triangle
base = float(input("Entrez la base: "))
hauteur = float(input("Entrez la hauteur: "))
area_triangle = 0.5 * base * hauteur
print("La zone du triangle est", area_triangle)

# 5. Périmètre du triangle
a = float(input("Entrez le côté A: "))
b = float(input("Entrez le côté B: "))
c = float(input("Entrez le côté C: "))
perimetre_triangle = a + b + c
print("Le périmètre du triangle est", perimetre_triangle)

# 6. Rectangle
longueur = float(input("Entrez la longueur: "))
largeur = float(input("Entrez la largeur: "))
surface_rectangle = longueur * largeur
perimetre_rectangle = 2 * (longueur + largeur)
print("Surface:", surface_rectangle, "Périmètre:", perimetre_rectangle)

# 7. Cercle
r = float(input("Entrez le rayon: "))
pi = 3.14
aire_cercle = pi * r * r
circumference = 2 * pi * r
print("Aire:", aire_cercle, "Circonférence:", circumference)

# 8. Pente, ordonnée de x, ordonnée de y où y = 2x - 2
m = 2
x_intercept = 2 / 2
y_intercept = -2

# 9. Pente et distance entre (2,2) et (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
m2 = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# 10. Comparer les pentes
print(m == m2)

# 11. Trouver y = x^2 + 6x + 9 pour différentes x
x = -3
y = x**2 + 6*x + 9
print(y)

# 12. Longueur Python et Dragon
print(len("Python") != len("Dragon"))

# 13. Vérifier 'on' dans python et dragon
print('on' in "python" and 'on' in "dragon")

# 14. Vérifier 'jargon' dans la phrase
phrase = "I hope this course is not full of jargon"
print("jargon" in phrase)

# 15. Vérifier 'on' non présent
print('on' not in "Python" and 'on' not in "Dragon")

# 16. Longueur Python, convertir en float et string
longueur_python = len("Python")
print(float(longueur_python))
print(str(longueur_python))

# 17. Vérifier si un nombre est pair
nombre = int(input("Entrez un nombre: "))
print(nombre % 2 == 0)

# 18. Vérifier floor division
print(7 // 3 == int(2.7))

# 19. Vérifier type "10" et 10
print(type("10") == type(10))

# 20. Vérifier int('9.8') == 10
# print(int('9.8') == 10)  # This causes an error because '9.8' is not an integer

# 21. Calculer rémunération
heures = float(input("Entrez les heures: "))
taux = float(input("Entrez le taux par heure: "))
salaire = heures * taux
print("Votre gain hebdomadaire est", salaire)

# 22. Nombre de secondes vécues
annees = int(input("Entrez le nombre d'années que vous avez vécu: "))
secondes = annees * 365 * 24 * 60 * 60
print("Vous avez vécu pendant", secondes, "secondes")

# 23. Tableau demandé
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")

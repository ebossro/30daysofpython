# 1. Déclarer une fonction add_two_numbers. Il prend deux paramètres et il renvoie une somme.
def add_two_numbers(a, b):
    return a + b

# 2. La zone d'un cercle est calculée comme suit: zone = π x r x r. Écrivez une fonction qui calcule area_of_circle.
def area_of_circle(r):
    return math.pi * r * r

# 3. Écrivez une fonction appelée add_all_nums qui prend un nombre arbitraire d'arguments et résume tous les arguments. Vérifiez si tous les éléments de la liste sont des types de nombres. Sinon, donnez un commentaire raisonnable.
def add_all_nums(liste_de_nombres):
    total = 0
    for item in liste_de_nombres:
        if isinstance(item, (int, float)):
            total += item
        else:
            return "Erreur : Tous les éléments de la liste doivent être des nombres pour pouvoir les additionner."
    return total

# 4. La température en ° C peut être convertie en ° F en utilisant cette formule: ° F = (° C X 9/5) + 32. Écrivez une fonction qui convertit ° C en ° F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 5. Écrivez une fonction appelée Check-Season, il faut un paramètre de mois et renvoie la saison: automne, hiver, printemps ou été.
def check_season(month):
    if month in ["septembre", "octobre", "novembre"]:
        return "automne"
    elif month in ["décembre", "janvier", "février"]:
        return "hiver"
    elif month in ["mars", "avril", "mai"]:
        return "printemps"
    else:
        return "été"

# 6. Écrivez une fonction appelée calcul_slope qui renvoie la pente d'une équation linéaire.
def calcul_slope(x1, y1, x2, y2):
    
    if x2 - x1 == 0:
        return "La pente est indéfinie (ligne verticale)."
    
    pente = (y2 - y1) / (x2 - x1)
    return pente

# 7. L'équation quadratique est calculée comme suit: ax2 + bx + c = 0. Écrivez une fonction qui calcule le jeu de solutions d'une équation quadratique, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):

    discriminant = b**2 - 4 * a * c

    if discriminant > 0:

        x1 = (-b + discriminant**0.5) / (2 * a)
        x2 = (-b - discriminant**0.5) / (2 * a)
        return f"Deux solutions réelles : x1 = {x1}, x2 = {x2}"
    elif discriminant == 0:

        x = -b / (2 * a)
        return f"Une seule solution réelle (double) : x = {x}"
    else:
        
        return "Pas de solutions réelles (les solutions sont complexes)."

# 8. Déclarer une fonction nommée print_list. Il prend une liste en tant que paramètre et il imprime chaque élément de la liste.
def print_list(liste):
    for item in liste:
        print(item)

# 9

def Reverse_List(tableau):

    liste_inversee = []
    
    for i in range(len(tableau) - 1, -1, -1):
        liste_inversee.append(tableau[i]) 
        
    return liste_inversee

# 10. Déclarer une fonction nommée CAPITalize_list_items. Il prend une liste en tant que paramètre et il renvoie une liste majuscule des éléments.
def capitalize_list_items(liste):
    return [item.upper() for item in liste]

# 11. Déclarer une fonction nommée add_item. Il prend une liste et un élément en tant que paramètre et il renvoie une liste avec l'élément ajouté.
def add_item(liste, item):
    liste.append(item)
    return liste

def add_item(liste, element):
    
    liste.append(element)
    return liste # On renvoie la liste après y avoir ajouté l'élément.

# 12

def add_item(liste, element):# La méthode .append() ajoute l'élément à la fin de la liste existante.
    liste.append(element)
    return liste 

# 13

def SUM_OF_NUMBERS(nombre):

    total = 0
    
    for i in range(nombre + 1):
        total += i 

    return total

# 14 

def SUM_OF_ODDS(nombre):
    
    total_impairs = 0
    
    for i in range(nombre + 1):
      
        if i % 2 != 0:
            total_impairs += i 

    return total_impairs

# 15. Déclarer une fonction nommée SUM_OF_EVEN. Il prend un paramètre de nombre et il ajoute tous les nombres pair dans cette plage.
def SUM_OF_EVEN(nombre):
    
    total_pairs = 0
    
    for i in range(nombre + 1):
        if i % 2 == 0:
            total_pairs += i

    return total_pairs

# Exercice 2
# 1

def evens_and_odds(nombre):
    
    count_evens = 0
    count_odds = 0

    for i in range(nombre + 1):
        if i % 2 == 0:  
            count_evens += 1
        else:  
            count_odds += 1

    print(f"Le nombre de cotes est de {count_odds}.")
    print(f"Le nombre d'Evens est de {count_evens}.")

# 2

def factorielle(n):
    
    if n < 0:
        return "Erreur : La factorielle n'est pas définie pour les nombres négatifs."
    
    elif n == 0:
        return 1
    
    else:
        resultat = 1
        for i in range(1, n + 1): 
            resultat *= i 
        return resultat

# 3

def is_empty(param):
    
    if not param:
        return True
    else:
        return False

# 4

def calculer_mean(liste):
    if not isinstance(liste, list):
        return "Erreur : Le paramètre doit être une liste."
    if not liste: 
        return 0 

    somme = 0
    nombre_elements = 0
    for element in liste:
        if isinstance(element, (int, float)):
            somme += element
            nombre_elements += 1
        else:
            return "Erreur : Tous les éléments de la liste doivent être des nombres."

    if nombre_elements == 0: 
        return "Erreur : La liste ne contient pas de nombres valides pour le calcul de la moyenne."

    return somme / nombre_elements

def calculer_median(liste):
    if not isinstance(liste, list):
        return "Erreur : Le paramètre doit être une liste."
    if not liste:
        return "Erreur : La liste est vide, pas de médiane possible."

    nombres_valides = []
    for element in liste:
        if isinstance(element, (int, float)):
            nombres_valides.append(element)
        else:
            return "Erreur : Tous les éléments de la liste doivent être des nombres pour calculer la médiane."

    if not nombres_valides:
        return "Erreur : La liste ne contient pas de nombres valides pour le calcul de la médiane."

    nombres_valides.sort() 
    n = len(nombres_valides)

    if n % 2 == 1: 
        return nombres_valides[n // 2]
    else: 
        milieu1 = nombres_valides[n // 2 - 1]
        milieu2 = nombres_valides[n // 2]
        return (milieu1 + milieu2) / 2

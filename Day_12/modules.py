import random

# 1

def list_of_hexa_colors(num_colors):
    """
    Génère une liste de couleurs hexadécimales.

    Args:
        num_colors (int): Le nombre de couleurs hexadécimales à générer.

    Returns:
        list: Une liste de chaînes de caractères représentant les couleurs hexadécimales.
    """
    hexa_chars = '0123456789abcdef'
    colors = []
    for _ in range(num_colors):
        hex_color = '#'
        for _ in range(6):
            hex_color += random.choice(hexa_chars)
        colors.append(hex_color)
    return colors

# 2

def list_of_rgb_colors(num_colors):
    """
    Génère une liste de couleurs RVB.

    Args:
        num_colors (int): Le nombre de couleurs RVB à générer.

    Returns:
        list: Une liste de chaînes de caractères représentant les couleurs RVB.
    """
    colors = []
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'RGB ({r}, {g}, {b})')
    return colors

# 3

def Generate_Colors(color_type, num_colors):
    """
    Génère des couleurs de type hexa ou RVB.

    Args:
        color_type (str): Le type de couleur à générer ('Hexa' ou 'RGB').
        num_colors (int): Le nombre de couleurs à générer.

    Returns:
        list: Une liste de chaînes de caractères représentant les couleurs.
    """
    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        return "Type de couleur non valide. Veuillez utiliser 'Hexa' ou 'RGB'."

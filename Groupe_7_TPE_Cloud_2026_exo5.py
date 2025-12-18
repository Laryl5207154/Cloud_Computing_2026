def compresser(texte):
    if not texte: return "" # Gestion cas vide
    
    resultat_liste = []
    compteur = 1
    
    for i in range(1, len(texte)):
        if texte[i] == texte[i-1]:
            compteur += 1
        else:
            # On ajoute à la liste au lieu de recréer une chaine
            resultat_liste.append(f"{texte[i-1]}{compteur}")
            compteur = 1
            
    # Le dernier groupe
    resultat_liste.append(f"{texte[-1]}{compteur}")
    
    return "".join(resultat_liste)

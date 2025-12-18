def verif_ip_standard(ip):

    # On utilise la méthode .split(".") pour couper la chaîne à chaque point.
    # Exemple : "192.168.1.1" devient la liste ['192', '168', '1', '1']
    octets = ip.split(".")
    
    # Une adresse IPv4 est constituée de strictement 4 octets.
    # Si on a 3 parties (192.168.1) ou 5 parties, c'est immédiatement faux.
    if len(octets) != 4:
        return False
        
    # On parcourt la liste des morceaux un à un pour les valider.
    for partie in octets:
        
        # Vérification du contenu (Est-ce que c'est des chiffres ?)
        # La méthode .isdigit() renvoie True seulement si la chaîne ne contient 
        # que des chiffres (0-9).
        # Cela permet d'éliminer :
        # Les lettres ("192.168.a.1")
        # Les chaînes vides (cas de "192..1.1")
        # Les nombres négatifs (car le signe "-" n'est pas un chiffre)
        if not partie.isdigit():
            return False
            
        # Conversion en entier
        # Maintenant qu'on est sûr que c'est "propre", on transforme 
        # la chaîne de caractères (ex: "255") en nombre entier (255)
        # pour pouvoir faire des comparaisons mathématiques.
        valeur = int(partie)
        
        # Vérification de la valeur (L'intervalle 0-255)
        # En réseau, un octet est codé sur 8 bits.
        # La valeur minimale est 0 (00000000) et maximale est 255 (11111111).
        # Si la valeur sort de cet intervalle, l'adresse est invalide.
        if not (0 <= valeur <= 255):
            return False
                   
    # Si on a parcouru toute la boucle sans trouver d'erreur (sans retourner False),
    # alors l'adresse respecte toutes les règles. On valide.
    return True
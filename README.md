LISTES DES MEMBRES DU GROUPE 7

23B276FS ABDOURAHAMAN ABB0 (Présent pendant l'échange sur le choix de l'agorithme de chaque exercice, proposition des commentaires dans le code python, proposition d'Algorithme)

25A155FS FOUEDJEU WOBENG YVES LARYL  (Proposition de l'agorithme final de chaque exercice, écriture du code python et publication sur GitHub)

24B507FS SOH CHENDJOU JUNIOR  (Présent pendant l'échange sur le choix de l'agorithme de chaque exercice, assistance lors de la publication sur GitHub et proposition d'Algorithme)

25A11FS SONCHIEU NGUETSE ANGE NERVEILLE (Proposition et présent pendant l'échange sur le choix de l'agorithme de chaque exercice)

25A074FS CHENDJOU SOKAMTE FRANCKY RDLY (Présent pendant l'échange sur le choix de l'agorithme de chaque exercice)

25A210FS  KEMADJOU TCHAKOTE KERRY BRYAN (Présent pendant l'échange sur le choix de l'agorithme de chaque exercice)

EXPLICATION DE LA RESOLUTION DU PROBLEME
Pour comprendre la logique du jeu du pendu de l'exercice 23 nous avons utiliser l'Algorithme ci dessous

ALGORITHME Jeu_du_pendu

VARIABLES

    secret_word : CHAINE
    masque : TABLEAU DE CARACTERES
    letter : CARACTERE
    final_word : CHAINE
    i, j : ENTIER
    
DEBUT

    secret_word <- "bonjour"
    size <- LONGUEUR(secret_word)
  
    // Initialisation du masque avec des '#'
    POUR j ALLANT DE 0 A size - 1 FAIRE
        masque[j] <- "#"
    FIN POUR

    AFFICHER "Jeu du pendu !!"

    // La contrainte : Exactement 6 propositions
    POUR i ALLANT DE 1 A 6 FAIRE
        AFFICHER "Essai n°", i, " : Entrez une lettre"
        LIRE letter
        
        // Vérification et mise à jour du masque
        POUR j ALLANT DE 0 A size - 1 FAIRE
            SI secret_word[j] = letter ALORS
                masque[j] <- lettre
            FIN SI
        FIN POUR
        
        // Affichage de l'état actuel (ex: b # n # # u #)
        AFFICHER masque
    FIN POUR

    // Phase finale
    AFFICHER "Les 6 essais sont finis. Proposez le mot complet :"
    LIRE mot_final

    SI final_word = secret_word ALORS
        AFFICHER "GAGNE"
    SINON
        AFFICHER "PERDU"
    FIN SI
FIN

Pour comprendre la logique du compresseur de texte simple de l'exercice 5 nous avons utiliser l'Algoritme ci dessous 

FONCTION Compresser(texte : CHAINE) RETOURNE CHAINE

    longueur <- LONGUEUR(texte)
    SI longueur == 0 ALORS RETOURNER ""

    resultat <- ""
    compteur <- 1
    
    // On commence au deuxième caractère (index 1) et on regarde derrière
    POUR i ALLANT DE 1 A longueur - 1 FAIRE
        lettre_actuelle <- texte[i]
        lettre_precedente <- texte[i-1]

        SI lettre_actuelle == lettre_precedente ALORS
            compteur <- compteur + 1
        SINON
            // Changement de lettre détecté : on archive la précédente
            resultat <- resultat + lettre_precedente + compteur
            compteur <- 1 // Reset
        FIN SI
    FIN POUR

    // On n'oublie pas d'ajouter le dernier groupe qui est resté en mémoire
    resultat <- resultat + texte[longueur - 1] + compteur

    RETOURNER resultat
FIN FONCTION

Pour comprendre la logique de la validation d'une adresse IP de l'exercice 6 nous avons utiliser l'Algoritme ci dessous 

FONCTION Verif_IP_Standard(ip : CHAINE) RETOURNE BOOLEEN

    // Étape 1 : Découper la chaîne par les points
    octets <- SPLIT(ip, ".")
    
    // Étape 2 : Vérifier qu'il y a exactement 4 parties
    SI LONGUEUR(octets) != 4 ALORS
        RETOURNER FAUX
    FIN SI

    // Étape 3 : Analyser chaque partie
    POUR CHAQUE morceau DANS octets FAIRE
        // On doit vérifier si c'est un nombre avant de convertir
        SI NON EST_NUMERIQUE(morceau) ALORS
            RETOURNER FAUX
        FIN SI

        valeur <- CONVERTIR_EN_ENTIER(morceau)

        // Vérification de l'intervalle 0-255
        SI valeur < 0 OU valeur > 255 ALORS
            RETOURNER FAUX
        FIN SI
    FIN POUR

    // Si on arrive ici, tout est bon
    RETOURNER VRAI
FIN FONCTION

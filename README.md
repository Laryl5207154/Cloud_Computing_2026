LISTES DES MEMBRES DU GROUPE 7

23B276FS ABDOURAHAMAN ABB0 (Présent pendant l'échange sur le choix de l'agorithme)

25A155FS FOUEDJEU WOBENG YVES LARYL  (Proposition de l'agorithme final, écriture du code python et publication sur GitHub)

24B507FS SOH CHENDJOU JUNIOR  (Présent pendant l'échange sur le choix de l'agorithme et assistance lors de la publication sur GitHub)

25A11FS SONCHIEU NGUETSE ANGE NERVEILLE (Proposition et présent pendant l'échange sur le choix de l'agorithme)

EXPLICATION DE LA RESOLUTION DU PROBLEME
Pour arriver à trouver une logique dans la conception du jeu on s'est fié à cette Algorithme ci dessous simple et efficace 

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

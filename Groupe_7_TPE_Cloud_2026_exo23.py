#Déclaration des variables et constante
#Détermination de la taille du mot à deviner et par la meme occasion attribuer un nombre de # égal à la taille du mot

secret_word = "bonjour"
masque = []
letter = " "

size = len(secret_word)

for j in range(0, size) :
    masque += "#"

#Afffichage du nom du Jeu

print("Jeu du Pendu")

#On repète la proposition d'entrer une lettre 6 et on s'assure que l'utilisateur entre bien une seule lettre 

for i in range(0, 7) :
    letter = input(f"Essai n° {i} : Entrer votre lettre_ ".lower())
    if len(letter) > 1 :
        print("Entrer un seul caractère. Meci !")
        letter = input(f"Essai n° {i} : Entrer votre lettre_ ".lower())

#On parcours chaque indice de caractère du mot à deviner
# en vérifiant si la valeur de l'indice à l'instant est égal à celle entrer par l'utilisateur
# lorsque c'est le cas, à cet indice dans le masque on remplace le # par la valeur de l'indice
# et que nous ne sommes pas au dernier indice on continue

    for j in range(0, size) :
        if secret_word[j] == letter :
            masque[j] = letter
    print(masque)

#On verifie si le mot proposé par l'utilisateur après ses six éssais correspond à celui qui servait de devinette
#en affichant Gagné si c'est le cas et Perdu dans le cas contraire  

final_word = input("Les 6 éssais sont finis. Proposez le mot complet : ".lower())
if final_word == secret_word :
    print("GAGNE")
else :
    print("PERDU")
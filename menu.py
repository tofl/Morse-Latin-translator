i = 1
while (i != 0) : # permet d'afficher le menu apres chaque choix
    print('1 pour la traduction latin -> morse')
    print('2 pour la traduction morse -> latin')
    print('3 pour quitter (n\'importe quelle touche)')
    ch = input('\nVotre choix : ')
    

    if (ch == '1') : # si l'utilisateur choisit 1 :
        from latin_morse import * # ...traduction latin -> morse
        print('\n\n') # retour a la ligne

    elif (ch == '2') : # si l'utilisateur choisit 2 :
        from morse_latin import * # ...traduction morse -> latin
        print('\n\n')

    elif (ch == '3') : # si l'utilisateur choisit 3 :
        print('Au revoir !') # fin du programme
        i = 0 # i = 0 alors la boucle s'arrete, le menu ne s'affiche plus

    else :
          print('Erreur')
          print('\n\n')

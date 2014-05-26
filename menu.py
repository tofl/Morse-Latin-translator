i = 1
while (i != 0) :
    print('1 pour la traduction latin -> morse')
    print('2 pour la traduction morse -> latin')
    print('3 pour quitter (n\'importe quelle touche)')
    ch = input('\nVotre choix : ')
    

    if (ch == '1') :
        from latin_morse import *
        print('\n\n')

    elif (ch == '2') :
        from morse_latin import *
        print('\n\n')

    elif (ch == '3') :
        print('Au revoir !')
        i = 0

    else :
          print('Erreur')
          print('\n\n')

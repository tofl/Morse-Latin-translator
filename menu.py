print('1 pour la traduction latin -> morse')
print('2 pour la traduction morse -> latin')
print('Autre pour quitter (n\'importe quelle touche)')
ch = input('\nVotre choix : ')
    

if (ch == '1') :
    from latin_morse import *

elif (ch == '2') :
    from morse_latin import *

else :
    print('Au revoir !')

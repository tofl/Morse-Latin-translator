print('1. Traduction latin -> morse')
print('2. Traduction morse -> latin')
print('3. Quitter (n\importe quelle touche')

ch = input('Votre choix : ')

if (ch == '1') :
    from latin_morse import *

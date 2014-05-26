from winsound import Beep # Import des modules
from time import sleep

latin=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
morse=['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/']

phrase = input('Entrez une phrase en majuscule : ') # l'utilisateur entre une phrase
i = 0 # Parcourt la chaine de caracteres
y = 0 # Parcourt liste latin
p_morse = '' # contient la traduction

while (i != len(phrase)) : # parcourt la chaine avec i
    if (phrase[i] != latin[y]) : # recherche l'equivalent du caractere de la chaine dans la liste latin
        y += 1 # si le caractere n'est pas trouvé, rechercher le caractere suivant

    else : # si le caractere equivalent est retrouvé :
        p_morse += morse[y] + ' ' # rajoute le caractere morse equivalent
            
        i += 1 # incremente i de 1
        y = 0 # remet y a 0 pour parcourir de nouveau la liste latin pour le caracteres suivant (i + 1)

# fin de la boucle la chaine est traduite

i = 0

# affichage de la traduction :
while (i != len(p_morse)) :
    
    if (p_morse[i] == '.') : # si le caractere est un point :
        sleep(0.08) # temps d'attente correspondant
        Beep(330,80) # son correspondant

    if (p_morse[i] == '-') : # si le caractere est un tiret :
        sleep(3 * 0.08)
        Beep(220,240)

    if (p_morse[i] == ' ') : # si le caractere est un espace :
        sleep(3 * 0.09)

    if (p_morse[i] == '/') : # si le caractere est une barre oblique :
        sleep(7 * 0.08)

    print(p_morse[i], end='') # affichage

    i += 1

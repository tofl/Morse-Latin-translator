latin=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
morse=['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/']

p_morse = input('Entrez du morse à traduire : ')
lettre = '' # variable lettre qui contiendra temporairement chaque lettre en morse
traduction = '' # stockera la traduction
i = 0

if (p_morse[-1] != ' ') : # verifie si le dernier caractere est un espace
    p_morse += ' '

while (i < len(p_morse)) :
    y = 0
    lettre += p_morse[i] # enregistre temporerement chaque caracteres morses d'une lettre

    if (p_morse[i] == ' ') : # si on arrive à la fin d'une lettre :
        
        lettre = lettre.replace(' ', '') # supprime les espaces
        
        while (y < len(morse)) : # parcours la liste morse pour rechercher le caractere correspondant
            
            if (morse[y] == lettre) : # si la lettre est retrouvee :
               traduction += latin[y] # on trouve son equivalent en latin
               lettre = '' # et on vide lettre pour recommencer
               
            y += 1
        
    i += 1

print(traduction) # affiche la traduction a la fin de la boucle principale

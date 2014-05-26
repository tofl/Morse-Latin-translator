latin=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
morse=['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/']

p_morse = input('Entrez du morse à traduire : ')
lettre = ''
traduction = ''
i = 0
y = 0

if (p_morse[-l] != ' ') :
    p_morse += ' '

while (i < len(p_morse)) :
    y = 0
    lettre += p_morse[i]

    if (p_morse[i] == ' ') :
        
        lettre = lettre.replace(' ', '')
        
        while (y < len(morse)) :
            
            if (morse[y] == lettre) :
               traduction += latin[y]
               lettre = ''
               
            y += 1
        
    i += 1

print(traduction)

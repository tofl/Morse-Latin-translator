from winsound import Beep
from time import sleep

latin=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
morse=['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','/']

phrase = input('Entrez une phrase en majuscule : ')
i = 0
y = 0
p_morse = ''

while (i != len(phrase)) :
    if (phrase[i] != latin[y]) :
        y += 1

    else :
        p_morse += morse[y] + ' '
            
        i += 1
        y = 0

i = 0

while (i != len(p_morse)) :
    
    if (p_morse[i] == '.') :
        sleep(0.08)
        Beep(330,80)

    if (p_morse[i] == '-') :
        sleep(3 * 0.08)
        Beep(220,240)

    if (p_morse[i] == ' ') :
        sleep(3 * 0.09)

    if (p_morse[i] == '/') :
        sleep(7 * 0.08)

    print(p_morse[i], end='')

    i += 1

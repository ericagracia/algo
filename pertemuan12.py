word = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

def said (n):
    if n < 10:
        return word[n]
    elif n >= 1_000_000_000:
        return said(n // 1_000_000_000) + ' billion ' + (said(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return said(n // 1_000_000) + ' million ' + (said(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        if n // 1_000 == 1:
            return " one thousand " + (said(n % 1_000) if n % 1_000 != 0 else '')
        else:
            return said(n // 1_000) + " thousand " + (said(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        if n // 100 == 1:
            return ' hundred ' + (said(n % 100) if n % 100 != 0 else '')
        else:
            return said(n // 100) + ' hundred ' + (said(n % 100) if n % 100 != 0 else '')
    elif n >= 20:
        if n//10 == 2:
            return 'twenty' + (said(n % 10) if n % 10 != 0 else ' ')
        elif n//10 == 3:
            return 'thirty' + (said(n % 10) if n % 10 != 0 else ' ')
        elif n//10 == 4:
            return 'fourty' + (said(n % 10) if n % 10 != 0 else ' ')
        elif n//10 == 5:
            return 'fifty' + (said(n % 10) if n % 10 != 0 else ' ')
        else:
            return said(n//10) + 'ty' + (said(n % 10) if n % 10 != 0 else ' ')        

    else:
        if n == 10:
            return 'ten'
        elif n == 11:
            return 'eleven'
        elif n == 12:
            return 'twelve'
        elif n == 13:
            return 'thirteen'
        elif n == 14:
            return 'fourteen'
        elif n == 15:
            return 'fifteen'
        else :
            return said( n % 10) + 'teen'

import os
while True:
    os.system('cls')
    try:
        n = int(input('Type Your Number'))
        print(f'{n:,} = {said(n)}')
    except:
        print('Not found, Please Try Again')
    os.system('pause')
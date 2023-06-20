chave = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
         'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
         'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
         'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
         '2': '..---', '3': '...--', '4': '....-',
                    '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.' }

while True:
    print('*'*40) ## Replica 40 vezes o valor que no caso aqui é '*'
    
    try:
        mensagem =str(input('Digite o texto a traduzir: ')).upper()
        morse = []
        for char in mensagem:
                if char in chave:
                    morse.append(chave[char])
                a = " ".join(morse)
        print(a)
    except:
        print("Tem caracteres não identificados ")
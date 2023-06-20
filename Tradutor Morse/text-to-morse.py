from time import sleep


##print('-'*40)


# In[ ]:


dataset = {'A': '.-',   'B': '-...',    'C': '-.-.',    'D': '-..',
       'E': '.',    'F': '..-.',    'G': '--.',     'H': '....',
       'I': '..',   'J': '.---',    'K': '-.-',     'L': '.-..',
       'M': '--',   'N': '-.',      'O': '---',     'P': '.--.',
       'Q': '--.-', 'R': '.-.',     'S': '...',     'T': '-',
       'U': '..-',  'V': '...-',    'W': '.--',     'X': '-..-',
       'Y': '-.--', 'Z': '--..',

       '0': '-----',    '1': '.----',   '2': '..---',   '3': '...--',
       '4': '....-',    '5': '.....',   '6': '-....',   '7': '--...',
       '8': '---..',    '9': '----.',   ' ': '\n'
        }
option = '1'


# In[ ]:


while option == '1':
    try:
        text = input('Digite aqui o texto: ').upper()

        morse = ' '

        for char in text:
            sleep(1)
            morse = dataset[char]
            if char != " ":
                print("{} = {}".format(char, morse))
            else:
                print(morse)

        sleep(0.5)

        print('Tradução completa!')
        print("Deseja traduzir outro texto?")
        option = input("1. Sim\n2. Não\n=> ")
        
    except KeyError as e:
        char_error = str(e).replace("\'", '')
        print('{} = Caractere não reconhecido'.format(char_error))
        print('Tente novamente!')
    except KeyboardInterrupt:
        option = '2'
        print('')

print("Você decidiu sair!")


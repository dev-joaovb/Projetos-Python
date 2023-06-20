def morse_para_texto(codigo_morse):
    # Dicionário com a tabela de tradução de código Morse para caracteres
    morse_para_caractere = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
        '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
        '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
        '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
        '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
        '--..': 'Z', '.----': '1', '..---': '2', '...--': '3',
        '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', '-----': '0', '/': ' '
    }
    
    codigo_morse = codigo_morse.strip()  # Remove espaços em branco do início e fim
    palavras = codigo_morse.split(' / ')  # Divide as palavras separadas por ' / '
    
    texto = ''
    for palavra in palavras:
        caracteres = palavra.split(' ')  # Divide os caracteres separados por espaços
        for caractere in caracteres:
            if caractere in morse_para_caractere:
                texto += morse_para_caractere[caractere]
            else:
                texto += '?'  # Caractere desconhecido, pode ser substituído por outra coisa se preferir
        texto += ' '  # Adiciona um espaço entre as palavras
    
    return texto.strip()  # Remove espaços em branco do início e fim

# Exemplo de uso
codigo_morse = "-..."
texto_traduzido = morse_para_texto(codigo_morse)
print(texto_traduzido)

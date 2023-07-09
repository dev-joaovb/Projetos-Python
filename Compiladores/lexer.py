import re 

# Define os padrões para os diferentes tipos de tokens
token_patterns = [
    ('KEYWORD', r'\b(program|begin|end|var|integer|real|if|then|else|while|do|writeln)\b'),
    ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('INTEGER', r'\d+'),
    ('REAL', r'\d+\.\d+'),
    ('OPERATOR', r'(\+|-|\*|/|:=|<|>)'),
    ('DELIMITER', r'(\(|\)|;|\.|,)'),
    ('COLON', r':'),
    ('WHITESPACE', r'\s+')
]

# Função para fazer a análise léxica
def tokenize(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None
        for token_type, pattern in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                token = (token_type, match.group(0))
                if token_type != 'WHITESPACE':
                    tokens.append(token)
                position = match.end()
                break
        
        if not match:
            raise ValueError(f"Invalid token: {code[position:position+1]} at position {position}")
    
    return tokens

# Exemplo de uso
file_path = 'pascal_code.txt'  # Replace with the actual file path

with open(file_path, 'r') as file:
    pascal_code = file.read()

tokens = tokenize(pascal_code)

for token_type, token_value in tokens:
    print(f'Token: {token_type}, Value: {token_value}')

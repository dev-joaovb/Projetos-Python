from lexer import tokenize, pascal_code

# Função para fazer a análise sintática
def parse(tokens):
    # Variável para acompanhar o índice do token atual
    current_token = 0

    # Função auxiliar para obter o próximo token
    def next_token():
        nonlocal current_token
        current_token += 1

    # Função auxiliar para verificar o tipo do token atual
    def check_token(token_type):
        return tokens[current_token][0] == token_type

    # Função auxiliar para verificar e consumir um token esperado
    def consume_token(token_type):
        nonlocal current_token
        if check_token(token_type):
            next_token()
        else:
            raise SyntaxError(f"Token '{token_type}' esperado, mas encontrado '{tokens[current_token][0]}'")

    # Funções para analisar cada regra da gramática

    def program():
        consume_token('KEYWORD')
        consume_token('IDENTIFIER')
        consume_token('DELIMITER')
        declarations()
        consume_token('KEYWORD')
        statement()
        consume_token('DELIMITER')
        consume_token('KEYWORD')
        consume_token('DELIMITER')

    def declarations():
        consume_token('KEYWORD')
        consume_token('IDENTIFIER')
        consume_token('COLON')
        consume_token('KEYWORD')
        consume_token('DELIMITER')

    def statement():
        consume_token('IDENTIFIER')
        consume_token('OPERATOR')
        expression()

    def expression():
        consume_token('INTEGER')
        consume_token('OPERATOR')
        consume_token('INTEGER')

    try:
        program()
        
        if current_token < len(tokens):
            raise SyntaxError("Tokens extras encontrados após o final do programa.")

        print("Análise sintática bem-sucedida.")
    except SyntaxError as e:
        print(f"Erro de sintaxe: {str(e)}")
    except IndexError:
        print("Erro: índice fora dos limites da lista.")

tokens = tokenize(pascal_code)
parse(tokens)
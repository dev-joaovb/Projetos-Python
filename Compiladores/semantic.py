from lexer import tokenize, pascal_code


symbol_table = {}

def analyze_semantics(tokens):
    current_token = 0

    def next_token():
        nonlocal current_token
        current_token += 1

    def check_token(token_type):
        return tokens[current_token][0] == token_type

    def consume_token(token_type):
        nonlocal current_token
        if check_token(token_type):
            next_token()
        else:
            raise SyntaxError(f"Token '{token_type}' esperado, mas encontrado '{tokens[current_token][0]}'")

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
        if check_token('KEYWORD') and tokens[current_token][1] == 'var':
            consume_token('KEYWORD')
            consume_token('IDENTIFIER')
            variable_name = tokens[current_token - 1][1]
            if variable_name in symbol_table:
                raise NameError(f"Variável '{variable_name}' já foi declarada")
            consume_token('COLON')
            consume_token('KEYWORD')
            variable_type = tokens[current_token - 1][1]
            symbol_table[variable_name] = variable_type
            consume_token('DELIMITER')

    def statement():
        consume_token('IDENTIFIER')
        variable_name = tokens[current_token - 1][1]
        if variable_name not in symbol_table:
            raise NameError(f"Variável '{variable_name}' não foi declarada")
        if symbol_table[variable_name] != 'integer':
            raise ValueError(f"Variável '{variable_name}' tem que ser do tipo 'integer'")
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

        print("Análise Semântica bem-sucedida.")
    except (SyntaxError, NameError, ValueError) as e:
        print(f"Erro de Semântica: {str(e)}")
    except IndexError:
        print("Erro: índice fora dos limites da lista.")


tokens = tokenize(pascal_code)
analyze_semantics(tokens)
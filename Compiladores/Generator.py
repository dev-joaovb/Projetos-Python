from lexer import tokenize, pascal_code

# Classe para representar o código intermediário
class IntermediateCode:
    def __init__(self):
        self.code = []
        self.current_temp = 1

    def add_instruction(self, opcode, operand1=None, operand2=None):
        instruction = {'opcode': opcode, 'operand1': operand1, 'operand2': operand2}
        self.code.append(instruction)

    def generate_temp(self):
        temp = f'T{self.current_temp}'
        self.current_temp += 1
        return temp

    def __str__(self):
        lines = []
        for i, instruction in enumerate(self.code):
            line = f'{i + 1}: {instruction["opcode"]}'
            if instruction['operand1'] is not None:
                line += f' {instruction["operand1"]}'
            if instruction['operand2'] is not None:
                line += f', {instruction["operand2"]}'
            lines.append(line)
        return '\n'.join(lines)

# Função para fazer a análise sintática
def parse(tokens):
    # Variável para acompanhar o índice do token atual
    current_token = 0

    # Objeto para representar o código intermediário
    intermediate_code = IntermediateCode()

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
        variable = tokens[current_token - 1][1]
        intermediate_code.add_instruction('lda', variable)
        consume_token('OPERATOR')
        expression()
        intermediate_code.add_instruction('sto')

    def expression():
        intermediate_code.add_instruction('ldc', tokens[current_token][1])
        consume_token('INTEGER')
        intermediate_code.add_instruction('adi')
        consume_token('OPERATOR')
        intermediate_code.add_instruction('ldc', tokens[current_token][1])
        consume_token('INTEGER')

    try:
        program()

        if current_token < len(tokens):
            raise SyntaxError("Tokens extras encontrados após o final do programa.")

        print("Análise sintática bem-sucedida.")
        print("Código intermediário:")
        print(intermediate_code)
        generate_code(intermediate_code)
    except SyntaxError as e:
        print(f"Erro de sintaxe: {str(e)}")

def generate_code(intermediate_code):
    code = []
    for instruction in intermediate_code.code:
        opcode = instruction['opcode']
        operand1 = instruction['operand1']
        if opcode == 'lda':
            code.append(f'LDA {operand1}')
        elif opcode == 'lod':
            code.append(f'LOD {operand1}')
        elif opcode == 'ldc':
            code.append(f'LDC {operand1}')
        elif opcode == 'adi':
            code.append('ADI')
        elif opcode == 'sto':
            code.append('STO')
    print("\nGenerated Code:")
    print('\n'.join(code))

tokens = tokenize(pascal_code)
parse(tokens)

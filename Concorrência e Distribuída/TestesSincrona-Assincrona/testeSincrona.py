## fechamento de uma empresa

import time

def calcular_impostos(faturamento): ### Imposto a pagar
    print(faturamento * 0.1)



def calcular_bonus_funcionarios(vendas): ## bonus dos funcionarios
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, "Bonus: ", venda * 0.05)
        time.sleep(1)

## Tanto calcular impostos quanto o Bonus dos funcionarios, são processos independentes

def fechamento():
    vendas = { ## Vendas dos funcionarios
        "Pedro": 1500,
        "João": 500,
        "Amanda": 5000
    }

    faturamento = 1000
    calcular_bonus_funcionarios(vendas) # calcula bonus dos funcionarios
    calcular_impostos(faturamento) # calcula imposto dos funcionarios
    print("finish")


fechamento()


## Esse processo executado é Sincrona, onde cada elemento
## é executado por vez
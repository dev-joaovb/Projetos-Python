## fechamento de uma empresa

import time
import asyncio # biblioteca async

async def calcular_impostos(faturamento): ### Imposto a pagar
    print(faturamento * 0.1)



async def calcular_bonus_funcionarios(vendas): ## bonus dos funcionarios
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, "Bonus: ", venda * 0.05)
        time.sleep(1)

## Tanto calcular impostos quanto o Bonus dos funcionarios, são processos independentes

async def fechamento():
    vendas = { ## Vendas dos funcionarios
        "Pedro": 1500,
        "João": 500,
        "Amanda": 5000
    }

    faturamento = 1000

    tarefa1 = asyncio.create_task(calcular_bonus_funcionarios(vendas)) # calcula bonus dos funcionarios
    tarefa2 = asyncio.create_task(calcular_impostos(faturamento)) # calcula imposto dos funcionarios
    print("finish")



asyncio.run(fechamento())

## Nessa execução, o print("finish") foi executado primeiro
## Isso pq de forma assincrona as demais funções estão em andamento
## Enquanto elas são executadas as tarefas 1 e 2 são agendadas
## Dessa forma o print("finish") é executada primeiro


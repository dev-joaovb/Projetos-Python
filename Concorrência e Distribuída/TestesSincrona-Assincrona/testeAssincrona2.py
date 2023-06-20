## fechamento de uma empresa

import time
import asyncio # biblioteca async

async def calcular_impostos(faturamento): ### Imposto a pagar
    print(faturamento * 0.1)



async def calcular_bonus_funcionarios(vendas): ## bonus dos funcionarios
    for funcionario in vendas:
        venda = vendas[funcionario]
        print(funcionario, "Bonus: ", venda * 0.05)
        await asyncio.sleep(1)


## Tanto calcular impostos quanto o Bonus dos funcionarios, são processos independentes

async def fechamento():
    vendas = { ## Vendas dos funcionarios
        "Pedro": 1500,
        "João": 500,
        "Amanda": 5000
    }

    faturamento = 1000 # imposto

    tarefa1 = asyncio.create_task(calcular_bonus_funcionarios(vendas)) # calcula bonus dos funcionarios
    tarefa2 = asyncio.create_task(calcular_impostos(faturamento)) # calcula imposto dos funcionarios
    print("finish")

    await tarefa1
    await tarefa2


asyncio.run(fechamento())

## Ponto importante dessa execução, o await serviu para esperar as tarefas agendadas serem executadas primeiro
# É importante entender que, o await ele garante a espera do carregamento completo
# das funções, ou seja, não corre o risco das funções carregarem de forma incompleta. 
 
#
# Outro ponto importante, a execução do await asyncio.sleep(1)
# Ele que faz o processo assincrona enquanto o tempo de carregamento de uma função acontece, outra função já está sendo executada


import math
import statistics

numeros = [
0.4248018963269199,
0.4856240915327356,
0.4875949449107997,
0.4599457943211463,
0.5623578295261232,
0.5697239746977411,
0.5139731097913463,
0.5874546246579459, 
0.6446746741343257,
0.5797181511378935 
]

print(statistics.mean(numeros))

### Medias Io_bound ####

## Media Um Processo
## Tempo médio: 8.661426496505737

## Media Multithreads
## Tempo médio: 4.6931877613067625

## Media Multiprocessing
## Tempo médio: 4.800922918319702

## Media Asyncio HTTP
## Tempo médio: 1.338638997077942

## Media Asyncio Manual
## Tempo médio: 2.0245226621627808



### Medias CPU_Bound ####

## Media Um Processo
## Tempo médio: 55.95888528823853

## Media Multitrhead
## Tempo médio: 49.480123901367186

## Media Asyncio
## Tempo médio: 53.558904504776

## Media Multiprocessing
## Tempo médio: 26.389539432525634
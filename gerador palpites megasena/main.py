
import uteis
from time import sleep

quant = int(input('Quantos jogos voce quer? '))

lista_jogos = uteis.sortear_palpites(quant)

print(uteis.linha("PALPITES PARA A MEGASENA"))

for i,jogo in enumerate(lista_jogos):
    print(f'jogo {i+1}:\t{jogo}')
    sleep(1)
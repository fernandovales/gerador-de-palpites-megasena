def linha(texto):
    print('-=' * 15)
    return f'{texto.center(30)}'


def sortear_palpites(quant):
    ''' gera bilhetes de jogos da megasena com 6 numeros 
    
    parameters:
        quant(int): quantidade de jogos
    
    returns:
        jogos(list): lista com os jogos
    '''
    from random import randint                             
    from time import sleep
    
    palpites = []
    jogos = []
    tot = 1
    
    while tot <= quant:                                    
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in palpites:
                palpites.append(num)
                cont += 1
            if cont >= 6:
                break
        palpites.sort()
        jogos.append(palpites[:])
        palpites.clear()
        tot += 1
    return jogos

    

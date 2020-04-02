from random import randint
# Função que simula Pass Line Bet
def Pass_Line_Bet(creditos, aposta_plb):
# lance e soma dos dados 
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma_dados = dado1 + dado2
    print('O lance dos dados deu: {}'.format(soma_dados))
    if soma_dados == 7 or soma_dados == 11:
        creditos += aposta_plb
        print('Parabéns, você ganhou!')
    elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        creditos -= aposta_plb
        print('Você perdeu.')
    else:
        falta_de_conclusao = True
        point = soma_dados
        print('Fase: "Point"')
        while falta_de_conclusao:
# Fase Point
            dado1 = randint(1,6)
            dado2 = randint(1,6)
            soma_dados = dado1 + dado2
            print('O lance dos dados deu: {}'.format(soma_dados))
            if point == soma_dados:
                creditos += aposta_plb
                print('Você ganhou!')
                falta_de_conclusao = False
            elif soma_dados == 7:
                creditos -= aposta_plb
                print('Você perdeu.')
                falta_de_conclusao = False
    return creditos
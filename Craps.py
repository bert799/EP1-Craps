""" Exercício 1 design de software EP1 
objetivo: simular jogo de apostas Craps
Autor: Bernardo Cunha Capoferri 
python ver.: 3.7.4 64-bit, Coded in VScode """

# Importa random integer
from random import randint

# Começo do jogo
def comeco_jogo():
# valor booleano que decide se o jogo deve continuar
    queroJogar = True
# Valor booleano que define fase do jogo
    comeOut = True
# creditos que o jogador possui
    creditos = 10000
# Loop de validação de vontade de continuar jogando
    while queroJogar:
# Imprime creditos
        print('Você tem {} créditos'.format(creditos))
# Aposta Pass Line Bet
        if comeOut:
            print('Fase: "Come Out"')
            aposta_plb = int(input('Quanto quer apostar no Pass Line Bet? '))
            if aposta_plb > creditos or aposta_plb < 0:
                print('Valor inválido por favor insira um valor válido.')
                continue
            creditos = Pass_Line_Bet(creditos, aposta_plb)
            print('Você tem {} fichas'.format(creditos))
# Função que simula Pass Line Bet
def Pass_Line_Bet(creditos, aposta_plb):
# lance e soma dos dados 
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma_dados = dado1 + dado2
    if soma_dados == 7 or soma_dados == 11:
        creditos += aposta_plb
        print('Parabéns, você ganhou!')
    elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        creditos -= aposta_plb
        print('Você perdeu.')
    else:
        comeOut = False
        falta_de_conclusao = True
        point = soma_dados
        print('Fase: "Point"')
# Fase Point
        while falta_de_conclusao:
            dado1 = randint(1,6)
            dado2 = randint(1,6)
            soma_dados = dado1 + dado2
            if point == soma_dados:
                creditos += aposta_plb
                print('Você ganhou!')
                falta_de_conclusao = False
            elif soma_dados == 7:
                creditos -= aposta_plb
                print('Você perdeu.')
                falta_de_conclusao = False
        return creditos


    
#inicializa programa
comeco_jogo()

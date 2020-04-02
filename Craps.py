""" Exercício 1 design de software EP1 
objetivo: simular jogo de apostas Craps
Autor: Bernardo Cunha Capoferri 
python ver.: 3.7.4 64-bit, Coded in VScode """

# Importa Funções das apostas
import FuncaoApostas as FA

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
            creditos = FA.Pass_Line_Bet(creditos, aposta_plb)

#inicializa programa
comeco_jogo()

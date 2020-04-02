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
        print('Você tem {} fichas'.format(creditos))
# Pergunta se quer continuar jogando
        cash_out = input('Você quer continuar jogando? ("s"/"n") ')
        if cash_out == 'n':
            print('Você terminou com {} fichas. muito obrigado por ter jogado!'.format(creditos))
            queroJogar = False
# Aposta Pass Line Bet
        if comeOut:
            print('Fase: "Come Out"')
            aposta_plb = int(input('Quanto quer apostar no Pass Line Bet? '))
# Checa valores digitados
            if aposta_plb > creditos or aposta_plb < 0:
                print('Valor inválido por favor insira um valor válido.')
                continue
            creditos -= aposta_plb
# Pergunta se quer fazer aposta field
        quer_fazer_aposta_field = input('Você quer fazer uma aposta Field? ("s"/"n") ')
# Checa Valores digitados
        if quer_fazer_aposta_field != 'n' and quer_fazer_aposta_field != 's':
            print('Letra inválida por favor insira uma letra válida.')
            continue
# Pergunta valor aposta Field
        if quer_fazer_aposta_field == 's':
            aposta_field = int(input('Quanto quer apostar na Field? '))
# Checa Valores digitados
            if aposta_field > creditos or aposta_field < 0:
                print('Valor inválido por favor insira um valor válido.')
                continue
            creditos -= aposta_field
# Pergunta se quer fazer aposta Any Craps
        quer_fazer_aposta_ACraps = input('Você quer fazer uma aposta Any Craps? ("s"/"n") ')
# Checa Valores digitados
        if quer_fazer_aposta_ACraps != 'n' and quer_fazer_aposta_ACraps != 's':
            print('Letra inválida por favor insira uma letra válida.')
            continue
# Pergunta valor aposta Any Craps
        if quer_fazer_aposta_ACraps == 's':
            aposta_ACraps = int(input('Quanto quer apostar no Any Craps? '))
# Checa Valores digitados
            if aposta_ACraps > creditos or aposta_ACraps < 0:
                print('Valor inválido por favor insira um valor válido.')
                continue
# Pergunta se quer fazer aposta Twelve
        quer_fazer_aposta_twelve = input('Você quer fazer uma aposta Twelve? ("s"/"n") ')
# Checa Valores digitados
        if quer_fazer_aposta_twelve != 'n' and quer_fazer_aposta_twelve != 's':
            print('Letra inválida por favor insira uma letra válida.')
            continue
# Pergunta valor aposta Twelve
        if quer_fazer_aposta_field == 's':
            aposta_twelve = int(input('Quanto quer apostar na Twelve? '))
# Checa Valores digitados
            if aposta_twelve > creditos or aposta_twelve < 0:
                print('Valor inválido por favor insira um valor válido.')
                continue
# Caso perca todas as fichas
        if creditos == 0:
            print('Você não tem mais fichas, o jogo acabou.')
            queroJogar = False
        
        
        

#inicializa programa
comeco_jogo()

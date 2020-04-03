""" Exercício 1 design de software EP1 
objetivo: simular jogo de apostas Craps
Autor: Bernardo Cunha Capoferri 
python ver.: 3.7.4 64-bit, Coded in VScode """

# Importa Funções das apostas e randint
import FuncaoApostas as FA
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
        print('Você tem {} fichas'.format(creditos))
# Pergunta se quer continuar jogando
        cash_out = input('Você quer continuar jogando? ("s"/"n") ')
        if cash_out == 'n':
            print('Você terminou com {} fichas. muito obrigado por ter jogado!'.format(creditos))
            queroJogar = False
            break
# Aposta Pass Line Bet
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
                creditos += aposta_plb
                continue
            creditos -= aposta_field
            # Caso não queira digitar valor este se torna 0
        elif quer_fazer_aposta_field == 'n':
            aposta_field = 0
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
                creditos += aposta_plb
                creditos += aposta_field
                continue
            creditos -= aposta_ACraps
            # Caso não queira digitar valor este se torna 0
        elif quer_fazer_aposta_ACraps == 'n':
            aposta_ACraps = 0
# Pergunta se quer fazer aposta Twelve
        quer_fazer_aposta_twelve = input('Você quer fazer uma aposta Twelve? ("s"/"n") ')
# Checa Valores digitados
        if quer_fazer_aposta_twelve != 'n' and quer_fazer_aposta_twelve != 's':
            print('Letra inválida por favor insira uma letra válida.')
            continue
# Pergunta valor aposta Twelve
        if quer_fazer_aposta_twelve == 's':
            aposta_twelve = int(input('Quanto quer apostar na Twelve? '))
# Checa Valores digitados
            if aposta_twelve > creditos or aposta_twelve < 0:
                print('Valor inválido por favor insira um valor válido.')
                creditos += aposta_plb
                creditos += aposta_field
                creditos += aposta_ACraps
                continue
            creditos -= aposta_twelve
            # Caso não queira digitar valor este se torna 0
        elif quer_fazer_aposta_twelve == 'n':
            aposta_twelve = 0
# valor randomizado geral para apostas
        dado1 = randint(1, 6)
        dado2 = randint(1, 6)
# Checa ganhou/perdeu Comeout ou se foi para fase point
        resultado_CO = FA.Pass_Line_Bet(aposta_plb, dado1, dado2)
        resultado_field = FA.field_bet(aposta_field, dado1,dado2)
        resultado_ACraps = FA.any_craps(aposta_ACraps, dado1, dado2)
        resultado_twelve = FA.twelve (aposta_twelve, dado1, dado2)
        soma_apostas_F_AC_T = resultado_ACraps + resultado_field + resultado_twelve
        if resultado_CO[0]:
            creditos += soma_apostas_F_AC_T + resultado_CO[1]
# Começo fase Point
        else:
            comeOut = False
            valor_point = resultado_CO[1]
            print('Fase: "Point""')
            print('O valor point é {}'.format(valor_point))
            while not comeOut:
                print('Você tem {} fichas'.format(creditos))
                dado1 = randint(1, 6)
                dado2 = randint(1, 6)
                # Repetição das perguntas da fase Come Out
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
                else:
                    aposta_field = 0
                # Pergunta aposta Any Craps
                quer_fazer_aposta_ACraps = input('Você quer fazer uma aposta Any Craps? ("s"/"n") ')
                if quer_fazer_aposta_ACraps != 'n' and quer_fazer_aposta_ACraps != 's':
                    print('Letra inválida por favor insira uma letra válida.')
                    continue
                if quer_fazer_aposta_ACraps == 's':
                    aposta_ACraps = int(input('Quanto quer apostar no Any Craps? '))
                    if aposta_ACraps > creditos or aposta_ACraps < 0:
                        print('Valor inválido por favor insira um valor válido.')
                        creditos += aposta_field
                        continue
                    creditos -= aposta_ACraps
                else:
                    aposta_ACraps = 0
                # Pergunta aposta twelve
                quer_fazer_aposta_twelve = input('Você quer fazer uma aposta Twelve? ("s"/"n") ')
                if quer_fazer_aposta_twelve != 'n' and quer_fazer_aposta_twelve != 's':
                    print('Letra inválida por favor insira uma letra válida.')
                    continue
                if quer_fazer_aposta_twelve == 's':
                    aposta_twelve = int(input('Quanto quer apostar na Twelve? '))
                    if aposta_twelve > creditos or aposta_twelve < 0:
                        print('Valor inválido por favor insira um valor válido.')
                        creditos += aposta_field
                        creditos += aposta_ACraps
                        continue
                    creditos -= aposta_twelve
                else:
                    aposta_twelve = 0
                # Começo da fase Point
                resultado_P = FA.fase_point(valor_point, aposta_plb, dado1, dado2)
                resultado_field = FA.field_bet(aposta_field, dado1, dado2)
                resultado_ACraps = FA.any_craps(aposta_ACraps, dado1, dado2)
                resultado_twelve = FA.twelve(aposta_twelve, dado1, dado2)
                soma_apostas_F_AC_T = resultado_ACraps + resultado_field + resultado_twelve
                # Checa se fase point alcançou o fim
                if resultado_P:
                    comeOut = True
                    creditos += soma_apostas_F_AC_T + resultado_P
                    break
                else:
                    creditos += soma_apostas_F_AC_T
        # Caso perca todas as fichas
        if creditos == 0:
            print('Você não tem mais fichas, o jogo acabou.')
            queroJogar = False
        

#inicializa programa
comeco_jogo()

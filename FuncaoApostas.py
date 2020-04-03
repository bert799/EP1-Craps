from random import randint
# Função que simula Pass Line Bet
def Pass_Line_Bet(aposta_plb, dado1, dado2):
# soma dos dados
    comeOut = True
    soma_dados = dado1 + dado2
    print('O lance dos dados deu: {}'.format(soma_dados))
    if soma_dados == 7 or soma_dados == 11:
        # Lucro tem que ser dobrado para  reflitir verdadeiros ganhos
        lucro = aposta_plb*2
        print('Parabéns, você ganhou a Pass line bet!')
        return comeOut, lucro
    elif soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        # ja subtrai quando perguntei o valor da aposta 
        prejuizo = 0
        print('Você perdeu a Pass Line Bet.')
        return comeOut, prejuizo
    else:
        comeOut = False
        return comeOut, soma_dados
# Função que simula fase Point
def fase_point(valor_point, aposta_plb, dado1, dado2):
    soma_dados = dado1 + dado2
    print('O lance dos dados deu: {}'.format(soma_dados))
    if soma_dados == valor_point:
        lucro = aposta_plb*2
        print('Parabéns, você ganhou a fase Point!')
        return lucro
    elif soma_dados == 7:
        prejuizo = 0
        print('Você perdeu a aposta Point.')
        return prejuizo
    else:
        print('Não ganhou nem perdeu, lance os dados de novo.')
        return False
# Função que simula aposta field
def field_bet(aposta_field, dado1, dado2):
    # Caso a aposta seja 0 não ocorre a operação
    if aposta_field == 0:
        return 0
    soma_dados = dado1 + dado2
    if soma_dados == 3 or soma_dados == 4 or soma_dados == 9 or soma_dados == 10 or soma_dados == 11:
        print('Parabéns, você ganhou a aposta Field!')
        lucro = aposta_field * 2
        return lucro
    elif soma_dados == 2:
        print('Você ganhou o DOBRO do que apostou na aposta Field!')
        lucro = aposta_field * 3
        return lucro
    elif soma_dados == 12:
        print('Jackpot! Você ganhou o TRIPLO do que apostou na aposta Field!')
        lucro = aposta_field * 4
        return lucro
    else:
        print('Você perdeu a aposta Field')
        prejuizo = 0
        return prejuizo
# Função que simula aposta Any Craps 
def any_craps(aposta_ACraps, dado1, dado2):
    # Caso a aposta seja 0 não ocorre a operação
    if aposta_ACraps == 0:
        return 0
    soma_dados = dado1 + dado2
    if soma_dados == 2 or soma_dados == 3 or soma_dados == 12:
        print('Você ganhou SETE vezes o que apostou na aposta Any Craps!')
        lucro = aposta_ACraps * 8
        return lucro
    else:
        print('Você perdeu a aposta Any Craps.')
        prejuizo = 0
        return prejuizo
# Função que simula aposta Twelve
def twelve(aposta_twelve, dado1, dado2):
    # Caso a aposta seja 0 não ocorre a operação
    if aposta_twelve == 0:
        return 0
    soma_dados = dado1 + dado2
    if soma_dados == 12:
        print('Você ganhou TRINTA vezes o que apostou na aposta Twelve!!!')
        lucro = aposta_twelve * 31
        return lucro
    else:
        print('você perdeu a aposta Twelve.')
        prejuizo = 0
        return prejuizo
            
    
    

    
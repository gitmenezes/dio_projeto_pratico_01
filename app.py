
#Programa: NTT DATA - Engenharia de Dados com Python
#Desafio de Projeto: Criando um Sistema Bancário com Python
##Atividade Proposta no Curso de Python do Instrutor: Guilherme Arthur de Carvalho
##Aluno: Alexandre Menezes Ferreira



mensagem_boas_vindas = "Bem vindos ao Sistema Bank 24hrs v1.0\n\n"
operacoes_disponiveis = 'Operações disponíveis: Depósitos, Saques e Extratos\n'
limites_operacionais = 'Limites Operacionais: 03 saques diários de R$500,00\n'


def boas_vindas():
    print("#"*70)
    print('\n',mensagem_boas_vindas, operacoes_disponiveis, limites_operacionais)

boas_vindas()

saldo = 1000
saque = 0
extrato = list()
limite_de_saque = 3

def controle_de_saques():
    global limite_de_saque
    if limite_de_saque > 0:
        limite_de_saque -= 1
        print('Saque realizado com sucesso!')
    else:
        print('Você atingiu seu limite de saque diário, não poderá realizar mais saques hoje. Consulte seu Gerente para outras opções e limites!')

def depositar():
    valor = int(input('Informe o valor que deseja depositar:\n'))
    if valor>0:
        global saldo
        saldo += valor
        print('Depósito realizado com sucesso!')
        extrato.append({'depósito':valor})
        #print(f'extrato:{extrato}')
        #print('Este é seu saldo:',saldo)
    else:
        print('Desculpe, o valor informado é inválido, por favor, tente novamente!')

        
def sacar():
    global saldo
    valor = int(input('informe o valor que deseja sacar:\n'))#limite de saque R$ 500,00 3/dia
    #print('saldo:',saldo)
    if valor <= saldo:
        if valor <= 500:
            saldo -= valor
            controle_de_saques()
            extrato.append({'saque':valor})
            #print(f'extrato:{extrato}',saldo)
        else:
            print('Valor não permitido, o valor do saque deve ser igual ou menor que R$ 500,00!')
    else:
        print('Atenção, saldo insuficiente!')


def extratos():
    #print(f'Extrato:\n{extrato}. Seu saldo atual é de: ' + "R$ %.2f" % saldo)
    for valor in extrato:
        print(valor)
    print(f'\nSeu saldo atual é de: ' + "R$ %.2f" % saldo + '\n')


def continuar_operacoes():
    continuar = int(input('Deseja realizar outra operação?\n[1]SIM\n[2]NÃO\n'))
    if continuar == 2:
        print('Operação finalizada com sucesso!')
        exit()
    elif continuar == 1:
        next    


def menu():
    smenu_escolha = int(input('Escolha uma das opções abaixo:\n[1] DEPÓSITO\n[2] SAQUE\n[3] EXTRATO\n[0] SAIR\n'))
    
    if smenu_escolha == 1:
        depositar()
        continuar_operacoes()

    elif smenu_escolha == 2:
        sacar()
        continuar_operacoes()  
    elif smenu_escolha == 3:
        extratos()
        continuar_operacoes()
    elif smenu_escolha == 0:
        print('Operação finalizada com sucesso!')
        exit()
    


    else:
        print('Operação finalizada com sucesso!')
        exit()

    

while True:
    print('#'*70)
    menu()
    print("#"*70)







    

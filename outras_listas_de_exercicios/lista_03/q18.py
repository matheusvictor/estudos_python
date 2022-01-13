# -*- coding: utf-8 -*-
saldo = 1000

login = raw_input("Informe login: ")
senha = int(input("Digite uma senha: "))

while(True):
    confirmaSenha = int(input("Repita a senha: "))

    if(senha == confirmaSenha):
        print("\nCadastrado com sucesso!")
        break
    else:
        print("\nAs senhas não conferem!")

while(True):
    confirmaLogin = raw_input("Digite o login para acessar o sistema: ")
    verificaSenha = int(input("Digite sua senha: "))

    if(confirmaLogin != login and verificaSenha == senha):
        print("\nLogin incorreto!")
    elif(confirmaLogin == login and verificaSenha != senha):
        print("Senha incorreta!")
    else:
        print("Login realizado com sucesso!")
        
        while(True):
            print("\nMENU:\n1- Verificar saldo\n2- Realizar depósito\n3- Realizar saque\n4-Sair")
            opc = int(input("\nDigite o número da operação desejada: "))

            while(opc > 4 or opc < 1):
                opc = int(input("\nOpção inválida! Digite novamente: "))
            
            if(opc == 1):
                print("Saldo: R${0}".format(saldo))
            elif(opc == 2):
                deposito = int(input("\nDigite o valor a ser depositado: R$"))
                saldo = saldo + deposito
            elif(opc == 3):
                saque = int(input("\nDigite o valor a ser sacado: R$"))
                saldo = saldo - saque
                print(saldo)
            else:
                break
# -*- coding: utf-8 -*-

continua = True

while(continua):
    nome = raw_input("Digite seu nome para realizar o login: ")
    senha = raw_input("Digite sua senha: ")

    if(nome == senha):
        print("Nome e senha não podem ser iguais!")
    else:
        print("OK!")
        continua = False
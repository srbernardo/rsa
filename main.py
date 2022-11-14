import os
from Func.encriptar import *
from Func.decriptar import *
from Func.chave_publica import *

def main():
   while True: 
    print("  <==================================================>")
    print("  <=                Projeto RSA                     =>")
    print("  <==================================================>")
    print("  <=        Escolha uma das opções á seguir:        =>")
    print("  <=                                                =>")
    print("  <= 1: GERAR CHAVE PUBLICA                         =>")
    print("  <= 2: ENCRIPTAR                                   =>")
    print("  <= 3: DESENCRIPTAR                                =>")
    print("  <= 0: SAIR                                        =>")
    print("  <==================================================>\n")
    escolha = int(input("Escolha uma opção: "))

    if(escolha == 1):
        chavePublica()
    elif(escolha == 2):
        rsa()
    elif(escolha == 3):
        mainDecriptar()
    elif(escolha == 0):
        break
    else:
        print("\n  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>")
        print("  <!!               Escolha inválida               !!>")
        print("  <!!               Digite novamente               !!>")
        print("  <!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>\n")
main()

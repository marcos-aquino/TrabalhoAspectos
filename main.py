#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Ian Couto - 201876002                                 #
# Marcos Aquino - 201276024                             #
#########################################################

import os

def printMenu():
    print("\nComando|                           Descrição                           |Exemplo")
    print(":d     |realiza a divisão em tags da string do arquivo informado       |:d input.txt")
    print(":c     |carrega um arquivo com definições de tags                      |:c tags.lex")
    print(":o     |especifica o caminho do arquivo de saída para a divisão em tags|:o output.txt")
    print(":p     |realiza a divisão em tags da entrada informada                 |:p x=1037")
    print(":a     |Lista as definições formais dos autômatos em memória           |:a")
    print(":l     |Lista as definições de tag válidas                             |:q")
    print(":q     |sair do programa                                               |:q")
    print(":s     |salvar as tags                                                 |:s file.txt\n")

#Le entradas do usuario ate que o comando :q seja digitado
while True:
    printMenu()
    entrada = input()
    while not entrada: #Evita erro de linha em branco
        entrada = input()
    #Reconhece os comandos iniciados com ':'
    if entrada[0] == ':':
        comando = entrada.split()
        if comando[0] == ':d':
            if len(comando) != 2:
                print ('[WARWING] Este comando precisa de 1 parametro!')
            else:
                print("[INFO] executar comando :d não implementado")
        elif comando[0] == ':c':
            if len(comando) != 2:
                print ('[WARWING] Este comando precisa de 1 parametro!')
            else:
                print("[INFO] executar comando :c não implementado")
        elif comando[0] == ':o':
            if len(comando) != 2:
                print ('[WARWING] Este comando precisa de 1 parametro!')
            else:
                print("[INFO] executar comando :o não implementado")
        elif comando[0] == ':p':
            if len(comando) != 2:
                print ('[WARWING] Este comando precisa de 1 parametro!')
            else:
                print("[INFO] executar comando :p não implementado")
        elif comando[0] == ':a':
            print("[INFO] executar comando :a não implementado")
        elif comando[0] == ':l':
            print("[INFO] executar comando :l não implementado")
        elif comando[0] == ':q':
            print("[INFO] executar comando :q não implementado")
            quit()
        elif comando[0] == ':s':
            if len(comando) != 2:
                print ('[WARWING] Este comando precisa de 1 parametro!')
            else:
                print("executar comando :s não implementado")
    #Usuario digitou uma tag (do tipo VAR: ab+c+x+) diretamente e ela precisa ser validada
    else:
        print("tag não reconhecida")
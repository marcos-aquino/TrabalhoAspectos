#########################################################
#   Trabalho DCC146 - Aspectos Teoricos da Computacao   #
# Grupo:                                                #
# Ian Couto - 201876002                                 #
# Marcos Aquino - 201276024                             #
#########################################################

import validacaoTags as valida
import gerenciaArquivo as arquivo

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

if __name__ == "__main__":
    conjunto_tags = [] #Conjunto de tags validas (tags invalidas nao sao armazenadas)

#Le entradas do usuario ate que o comando :q seja digitado
while True:
    printMenu()
    entrada = input()
    while not entrada: #Evita erro de linha em branco
        entrada = input()
    #Reconhece os comandos iniciados com ':'
    if entrada[0] == ':':
            comando = entrada.split()
            if comando[0] == ':q':
                print ('[INFO] Encerrando programa.')
                quit()
            elif comando[0] == ':s':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de 1 parametro!')
                else:
                    arquivo.salvaArquivo(comando[1], conjunto_tags)
            elif comando[0] == ':l':
                if len(comando) != 2:
                    print ('[WARN] Este comando precisa de 1 parametro!')
                else:
                    arquivo.importaArquivo(comando[1], conjunto_tags)
            elif comando[0] == ':d':
                print ('[INFO] Comando para realizar a divisao de tags do arquivo ainda nao implementado!')
            elif comando[0] == ':o':
                print ('[INFO] Comando para especificar o caminho do arquivo de saida ainda nao implementado!')
            elif comando[0] == ':p':
                print ('[INFO] Comando para realizar a divisao de tags da entrada ainda nao implementado!')
            elif comando[0] == ':a':
                print ('[INFO] Comando para listar as definições formais dos autômatos em memória ainda nao implementado!')
            elif comando[0] == ':c':
                print ('[INFO] Comando para carregar um arquivo com definições de tags ainda nao implementado!')                
            else:
                print ('[ERROR] Comando invalido!')
        #Usuario digitou uma tag (do tipo VAR: ab+c+x+) diretamente e ela precisa ser validada
    else:
        if valida.verificaFormato(entrada, conjunto_tags):
            if valida.validaTag(entrada):
                conjunto_tags.append(entrada+'\n')
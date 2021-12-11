import os
import time

#Aqui vai verificar se a dependencia youtube dl esta instalada
def verificacao():
    a = os.system("youtube-dl")
    os.system("clear")
    if a == 32512:
        print("Youtube-dl não existe! \nDependencia necessaria para baixar videos")
        print("Digite s para instalar. Caso não queira digite qualquer tecla")
        verificar = input()
        if verificar == 's':
            os.system("clear")
            os.system("pip3 install youtube-dl")
            verificacao = 1
            os.system("clear")
        else:
            print("Dependencia necessaria!!")
            verificacao = 0
    else:
        print("Depencia youtube-dl esta OK")
        verificacao = 1
        time.sleep(1)
        os.system("clear")
    return verificacao

#inicia em si o programa
def inicializacao(verif):
    if verif == 1:
        print("Bem vindo ao DownLoadVideo")
        link = input("Copie o link aqui: ")
        print("Arquivo a Baixar...")
        os.system("youtube-dl " + str(link))
        print("\nArquivo baixado com sucesso!!")
    return verif

#solicita verificação e retorna o valor 
verificacao = verificacao()

#Solicita a inicialização caso seja 1 o valor retornado
while verificacao == 1:
    vericacao = inicializacao(verificacao)
    sair = input("Deseja continuar? Digite 0 para sair ")
    os.system("clear")
    if sair == '0':
        break

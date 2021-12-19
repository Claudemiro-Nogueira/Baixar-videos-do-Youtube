import os
import time
from pytube import YouTube
from tkinter import *

#Aqui vai verificar se a dependencia youtube dl esta instalada

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



def procurar_arquivo(link):
    yt = YouTube(link)
    cwd = os.getcwd()
    print(cwd)
    os.system("cd "+ "'" + str(cwd)+ "'")
    q = len(yt.title) - len(yt.title) + 5
    lb1["text"] = "Arquivo neste diretorio\n" + cwd

#inicia em si o programa
def inicializacao():
    link1 = ent1.get()
    link = link1
    lb["text"] = "Arquivo Baixando...Aguarde"
    os.system("youtube-dl " + str(link))
    lb["text"] = "Arquivo baixado com\nsucesso"
    procurar_arquivo(link)
    print("\nArquivo baixado com sucesso!!")
 
def sobre():
    lb["text"] = "By Claudemiro-Nogueira\nGITHUB\nVaersão: 0.0.1"


janela = Tk()
janela.title("DLV - DownLoad Video")

ent1 = Entry(janela, width= 23)
ent1.place(x= 100, y = 100)

bt = Button(janela, text= "Baixar", width= 20, command = inicializacao)
bt.place(x = 100, y =150)
bt = Button(janela, text= "Sobre", width= 20, command = sobre)
bt.place(x = 100, y =200)

lb = Label(janela, text = "Cole seu link abaixo")
lb.place(x = 125,y = 20)
lb1 = Label(janela, text = " ")
lb1.place(x = 125,y = 55)
janela.geometry("400x300+200+200")
janela.mainloop()


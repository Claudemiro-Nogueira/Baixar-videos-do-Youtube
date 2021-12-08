import os

print("Bem vindo ao DownLoadVideo")
link = input("Copie o link aqui: ")

print("Arquivo a Baixar...")
os.system("youtube-dl " + str(link))

print("\n Arquivo baixado com sucesso!!")

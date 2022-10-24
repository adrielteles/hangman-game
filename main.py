from modules.player import Player
from modules.forca import Forca



while True:
    try:
            options_menu = ("1.SOLO", "2.VS", "3.Score Board", "4.Sair","\n")
            print("--------------FORCA-----------------","\n")
            for option in options_menu:
                print(option)
            print("--------------------------------------","\n")
            
            option = int(input('Selecionar Opção: '))
            if option in range(1, len(options_menu)+1):
                if option == 1:
                    forca_1 = Forca("SOLO")
                    forca_1.desenha_forca()
                elif option == 2:
                    print("modo versus")
                elif option == 3:
                    print("Score Board")
                elif option == 4:
                    print("Sai mesmo perdedor")
                    break
    except ValueError:
        print("Opção invalida")
    except EOFError:
        break

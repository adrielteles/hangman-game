from modules.game import Game


game = Game()
while True:
    try:
            options_menu = ("1.SOLO", "2.VS", "3.Score Board", "4.Sair","\n")
            print("--------------FORCA-----------------","\n")
            for option in options_menu:
                print(option)
            print("--------------------------------------","\n")
            
            option = int(input('Selecionar Opção: '))
            if option in range(1, len(options_menu)):
                if option == 1:
                    game.play(1)
                elif option == 2:
                    game.play(2)
                elif option == 3:
                    print("Score Board")
                elif option == 4:
                    print("Sai mesmo perdedor")
                    break
            else:
                print("opção invalida")
    except ValueError:
        print("Opção invalida")
    except EOFError:
        break

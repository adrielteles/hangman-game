from src.forca import Forca
from src.player import Player
from pathlib import Path

while True:
    try:
        options_menu = ('SOLO','VS','LIST OF PLAYERS','SAIR')
        print('JOGO DA FORCA',end='\n')
        i=1
        for opt in options_menu:
            print(i,' ',opt)
            i+=1
        print('-'*100)
        option = int(input('Opção: '))
        if option <=len(options_menu):
            if option == 1:
                forca_solo = Forca()
                forca_solo.setTemas()
                player_solo = Player()
                print('MODO', options_menu[0])
                nome_player = input("Nome Jogador: ")
                player_solo.procuraPlayer(nome_player)
                player_solo.calculaExp()
                player_solo.calculaLevel()
                player_solo.calculaPatente()
                while forca_solo.getTema() == '':
                    print('Escolha o tema')
                    i=1
                    for tema in forca_solo.getTemas():
                        print(i,' ',tema)
                        i+=1
                    option_tema = int(input('Escolha um tema: '))
                    if option_tema <= len(forca_solo.getTemas()):
                        forca_solo.setTema(forca_solo.getTemas()[option_tema-1])
                    else:
                        print('Tema não existe ainda')
                        continue
                forca_solo.setRandomPalavraSecreta()

                while True:
                    print('MODO', options_menu[0])
                    print(f'Player: {player_solo.getNome()} Palavras: {player_solo.getPalavrasAcertadas()} Letras: {player_solo.getLetrasAcertadas()} Exp: {player_solo.getExp()} Lv {player_solo.getLevel()} {player_solo.patenteIcon()} {player_solo.getPatente()}')
                    forca_solo.desenhaforca(forca_solo.formaPalavra(),forca_solo.getErros())
                    print(f'Palavras já usadas: {forca_solo.getLetrasUsadas()}')
                    chute = input("Chute: ")
                    if len(chute)> 1:
                        print("digite apenas uma letra.")
                        continue
                    forca_solo.setLetra(chute)

                    if forca_solo.winner(forca_solo.getErros()):
                        print('Você Ganhou!! Parabéns!')
                        print(f'Palavra Acertada: {forca_solo.getPalavraSecreta()} +5xp')
                        countLetras = len(forca_solo.getPalavraSecreta().replace(' ',''))
                        print(f'Letras acertadas: {countLetras} +{countLetras*2}xp')
                        player_solo.palavraAcertadas(1)
                        player_solo.letrasAcertadas(countLetras)
                        player_solo.savePlayer()
                        print(f'Player: {player_solo.getNome()} Palavras: {player_solo.getPalavrasAcertadas()} Letras: {player_solo.getLetrasAcertadas()} Exp: {player_solo.getExp()} Lv {player_solo.getLevel()} {player_solo.patenteIcon()} {player_solo.getPatente()}')
                        break
                    elif forca_solo.loser(forca_solo.getErros()):
                        forca_solo.desenhaforca(forca_solo.formaPalavra(),forca_solo.getErros())
                        print('Voce Perdeu!!')
                        print(f'A palavra era {forca_solo.getPalavraSecreta()}')
                        break
            elif option == 2:
                print(options_menu[1])
            elif option == 3:
                print(f'{"LIST OF PLAYERS":^101}')
                print("-----------------------------------------------------------------------------------")
                print(f'{"Nro":<5}{"Nome":<15}{"Total Palavras":<20}{"Total Letras":<15}{"Total Exp":<15}{"Lv.":<5}{"Patente":<15}')
                print("-----------------------------------------------------------------------------------")
                rankPlayer = 1
                caminho = Path(f'database/players')
                for arquivo in caminho.iterdir():
                    arquivo = open(f'{caminho}/{arquivo.name}', 'r')
                    player = arquivo.readline()
                    arquivo.close()
                    itens_player = player.split(',')
                    patente = ''
                    if itens_player[5] == 'Duck':
                        patente = '🦆'
                    elif itens_player[5] == 'Koala':
                        patente = '🐨'
                    elif itens_player[5] == 'Skunk':
                        patente = '🦨'
                    elif itens_player[5] == 'Cow':
                        patente = '🐮'
                    elif itens_player[5] == 'Panda':
                        patente = '🐼'
                    elif itens_player[5] == 'Unicorn':
                        patente = '🐨'
                    elif itens_player[5] == 'Dragon':
                        patente = '🐲'
                    print(f'{rankPlayer:<5}{itens_player[0]:<15}{itens_player[1]:^20}{itens_player[2]:^15}{itens_player[3]:^15}{itens_player[4]:^5}{patente} {itens_player[5]}')
                    rankPlayer += 1

            elif option == 4:
                print(options_menu[3])
                break
        else:
            print('Opção invalida')
    except ValueError:
        print('Opção invalida')
    except EOFError:
        break
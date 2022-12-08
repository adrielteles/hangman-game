from src.forca import Forca
from src.player import Player
from pathlib import Path
import time

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
                name_player = input("Nome Jogador: ")
                player_solo.procuraPlayer(name_player)
                player_solo.calculaExp()
                player_solo.calculaLevel()
                player_solo.calculaPatente()
                while forca_solo.getTema == '':
                    print('Escolha o tema')
                    i=1
                    for tema in forca_solo.getTemas:
                        print(i,' ',tema)
                        i+=1
                    option_tema = int(input('Escolha um tema: '))
                    if option_tema <= len(forca_solo.getTemas):
                        forca_solo.setTema(forca_solo.getTemas[option_tema-1])
                    else:
                        print('Tema não existe ainda')
                        continue
                forca_solo.setRandomPalavraSecreta()

                while True:
                    print('MODO', options_menu[0])
                    print(f'Player: {player_solo.name} Palavras: {player_solo.palavras_acertadas} Letras: {player_solo.letras_acertadas} Exp: {player_solo.exp} Lv {player_solo.level} {player_solo.patenteIcon()} {player_solo.patente}')
                    forca_solo.desenhaforca(forca_solo.formaPalavra(),forca_solo.getErros)
                    print(f'Palavras já usadas: {forca_solo.getLetrasUsadas}')
                    chute= input("Chute: ")
                    if len(chute)> 1:
                        print("digite apenas uma letra.")
                        continue
                    forca_solo.setLetra(chute.upper())

                    if forca_solo.winner(forca_solo.getErros):
                        forca_solo.desenhaforca(forca_solo.formaPalavra(),forca_solo.getErros)
                        print('Você Ganhou!! Parabéns!')
                        print(f'Palavra Acertada: {forca_solo.getPalavraSecreta} +5xp')
                        countLetras = len(forca_solo.getPalavraSecreta.replace(' ',''))
                        print(f'Letras acertadas: {countLetras} +{countLetras*2}xp')
                        player_solo.palavras_acertadas = 1
                        player_solo.letras_acertadas = countLetras
                        player_solo.savePlayer()
                        print(f'🏆 Player: {player_solo.name} Palavras: {player_solo.palavras_acertadas} Letras: {player_solo.letras_acertadas} Exp: {player_solo.exp} Lv {player_solo.level} {player_solo.patenteIcon()} {player_solo.patente}')
                        break
                    elif forca_solo.winner(forca_solo.getErros) == False:
                        forca_solo.desenhaforca(forca_solo.formaPalavra(),forca_solo.getErros)
                        print('Voce Perdeu!!')
                        print(f'A palavra era {forca_solo.getPalavraSecreta}')
                        break
            elif option == 2:
                forca_p1 = Forca()
                player_1 = Player()
                forca_p1.setTemas()

                forca_p2 = Forca()
                player_2 = Player()
                forca_p2.setTemas()


                print('MODO', options_menu[1])
                name_player_1 = input("Name player 1: ")
                player_1.procuraPlayer(name_player_1)
                player_1.calculaExp()
                player_1.calculaLevel()
                player_1.calculaPatente()
                while forca_p1.getTema == '':
                    print('Escolha o tema player 1')
                    i=1
                    for tema in forca_p1.getTemas:
                        print(i,' ',tema)
                        i+=1
                    option_tema = int(input('Escolha um tema: '))
                    if option_tema <= len(forca_p1.getTemas):
                        forca_p1.setTema(forca_p1.getTemas[option_tema-1])
                    else:
                        print('Tema não existe ainda')
                        continue
                
                print('MODO', options_menu[1])
                name_player_2 = input("Name player 2: ")
                player_2.procuraPlayer(name_player_2)
                player_2.calculaExp()
                player_2.calculaLevel()
                player_2.calculaPatente()
                while forca_p2.getTema == '':
                    print('Escolha o tema player 1')
                    i=1
                    for tema in forca_p2.getTemas:
                        print(i,' ',tema)
                        i+=1
                    option_tema = int(input('Escolha um tema: '))
                    if option_tema <= len(forca_p2.getTemas):
                        forca_p2.setTema(forca_p2.getTemas[option_tema-1])
                    else:
                        print('Tema não existe ainda')
                        continue
                forca_p1.setRandomPalavraSecreta()
                forca_p2.setRandomPalavraSecreta()

                while True:
                    print('MODO', options_menu[1])
                    print(f'Player: {player_1.name} Palavras: {player_1.palavras_acertadas} Letras: {player_1.letras_acertadas} Exp: {player_1.exp} Lv {player_1.level} {player_1.patenteIcon()} {player_1.patente}')
                    forca_p1.desenhaforca(forca_p1.formaPalavra(),forca_p1.getErros)
                    print(f'Palavras já usadas: {forca_p1.getLetrasUsadas}')
                    chute_p1 = input("Chute: ")
                    if len(chute_p1)> 1:
                        print("digite apenas uma letra.")
                        continue
                    forca_p1.setLetra(chute_p1.upper())

                    if forca_p1.winner(forca_p1.getErros):
                        forca_p1.desenhaforca(forca_p1.formaPalavra(),forca_p1.getErros)
                        print(f'{player_1.name} Ganhou!! Parabéns!')
                        print(f'Palavra Acertada: {forca_p1.getPalavraSecreta} +5xp')
                        countLetras_p1 = len(forca_p1.getPalavraSecreta.replace(' ',''))
                        print(f'Letras acertadas: {countLetras_p1} +{countLetras_p1*2}xp')
                        player_1.palavras_acertadas = 1
                        player_1.letras_acertadas = countLetras_p1
                        player_1.savePlayer()
                        print(f'1º🏆 Player: {player_1.name} Palavras: {player_1.palavras_acertadas} Letras: {player_1.letras_acertadas} Exp: {player_1.exp} Lv {player_1.level} {player_1.patenteIcon()} {player_1.patente}')
                        print(f'2º😿 Player: {player_2.name} Palavras: {player_2.palavras_acertadas} Letras: {player_2.letras_acertadas} Exp: {player_2.exp} Lv {player_2.level} {player_2.patenteIcon()} {player_2.patente}')
                        break
                    elif forca_p1.winner(forca_p1.getErros) == False:
                        forca_p1.desenhaforca(forca_p1.formaPalavra(),forca_p1.getErros)
                        print(f'{player_1.name} Perdeu!!')
                        print(f'A palavra era {forca_p1.getPalavraSecreta}')
                        print()
                        print('-'*100)
                        forca_p2.desenhaforca(forca_p2.formaPalavra(),forca_p2.getErros)
                        print(f'{player_2.name} Ganhou!! Parabéns!')
                        print(f'Palavra Acertada: {forca_p2.getPalavraSecreta} +5xp')
                        countLetras_p2 = len(forca_p2.getPalavraSecreta.replace(' ',''))
                        print(f'Letras acertadas: {countLetras_p2} +{countLetras_p2*2}xp')
                        player_2.palavras_acertadas = 1
                        player_2.letras_acertadas = countLetras_p2
                        player_2.savePlayer()
                        print(f'1º🏆 Player: {player_2.name} Palavras: {player_2.palavras_acertadas} Letras: {player_2.letras_acertadas} Exp: {player_2.exp} Lv {player_2.level} {player_2.patenteIcon()} {player_2.patente}')
                        print(f'2º😿 Player: {player_1.name} Palavras: {player_1.palavras_acertadas} Letras: {player_1.letras_acertadas} Exp: {player_1.exp} Lv {player_1.level} {player_1.patenteIcon()} {player_1.patente}')
                        
                        break
                    forca_p1.desenhaforca(forca_p1.formaPalavra(),forca_p1.getErros)
                    time.sleep(3)


                    print('MODO', options_menu[1])
                    print(f'Player: {player_2.name} Palavras: {player_2.palavras_acertadas} Letras: {player_2.letras_acertadas} Exp: {player_2.exp} Lv {player_2.level} {player_2.patenteIcon()} {player_2.patente}')
                    forca_p2.desenhaforca(forca_p2.formaPalavra(),forca_p2.getErros)
                    print(f'Palavras já usadas: {forca_p2.getLetrasUsadas}')
                    chute_p2 = input("Chute: ")
                    if len(chute_p2)> 1:
                        print("digite apenas uma letra.")
                        continue
                    forca_p2.setLetra(chute_p2.upper())

                    if forca_p2.winner(forca_p2.getErros):
                        forca_p2.desenhaforca(forca_p2.formaPalavra(),forca_p2.getErros)
                        print(f'{player_2.name} Ganhou!! Parabéns!')
                        print(f'Palavra Acertada: {forca_p2.getPalavraSecreta} +5xp')
                        countLetras_p2 = len(forca_p2.getPalavraSecreta.replace(' ',''))
                        print(f'Letras acertadas: {countLetras_p2} +{countLetras_p2*2}xp')
                        player_2.palavras_acertadas = 1
                        player_2.letras_acertadas = countLetras_p2
                        player_2.savePlayer()
                        print(f'1º🏆 Player: {player_2.name} Palavras: {player_2.palavras_acertadas} Letras: {player_2.letras_acertadas} Exp: {player_2.exp} Lv {player_2.level} {player_2.patenteIcon()} {player_2.patente}')
                        print(f'2º😿 Player: {player_1.name} Palavras: {player_1.palavras_acertadas} Letras: {player_1.letras_acertadas} Exp: {player_1.exp} Lv {player_1.level} {player_1.patenteIcon()} {player_1.patente}')
                        break
                    elif forca_p2.winner(forca_p2.getErros) == False:

                        forca_p1.desenhaforca(forca_p1.formaPalavra(),forca_p1.getErros)
                        print(f'{player_1.name} Ganhou!! Parabéns!')
                        print(f'Palavra Acertada: {forca_p1.getPalavraSecreta} +5xp')
                        countLetras_p1 = len(forca_p2.getPalavraSecreta.replace(' ',''))
                        print(f'Letras acertadas: {countLetras_p1} +{countLetras_p1*2}xp')
                        forca_p1.palavras_acertadas = 1
                        forca_p1.letras_acertadas = countLetras_p1
                        forca_p1.savePlayer()
                        print(f'1º🏆 Player: {player_1.name} Palavras: {player_1.palavras_acertadas} Letras: {player_1.letras_acertadas} Exp: {player_1.exp} Lv {player_1.level} {player_1.patenteIcon()} {player_1.patente}')
                        print(f'2º😿 Player: {player_2.name} Palavras: {player_2.palavras_acertadas} Letras: {player_2.letras_acertadas} Exp: {player_2.exp} Lv {player_2.level} {player_2.patenteIcon()} {player_2.patente}')
                        
                        break
                    forca_p2.desenhaforca(forca_p2.formaPalavra(),forca_p2.getErros)
                    time.sleep(5)


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
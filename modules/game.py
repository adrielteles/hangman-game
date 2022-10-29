from modules.forca import Forca
#from player import Player

class Game:

    def __init__(self) -> None:

        self.__modo = ""
        self.__forca_1 = Forca()
        self.__forca_2 = Forca()
        #self.__player_1 = Player()

    def escolhe_modo(self, modo:int):
        
        if modo == 1:
            self.__modo = "SOLO"
        if modo == 2:
            self.__modo = "VS"
        return self.__modo

    def ver_modo(self):
        return self.__modo

    def desenha_cabecalo(self):
        
        espacamento = "="*40
        print(f'{espacamento}\n {f"JOGO DA FORCA MODO {self.__modo}":^40} \n{espacamento}')


    def desenha_forca(self,erros):
        pass


    def play(self, modo: int):

        self.escolhe_modo(modo)
        if self.__modo == 'SOLO':
            self.__forca_1.escolhe_palavra()
            palavra_secreta = self.__forca_1.visualisa_palavra()
            letras_acertadas = self.__forca_1.display_palavra(palavra_secreta)
            erros = 0
            letras_faltando = len(letras_acertadas)
            acertou = False
            enforcou = False
            
            while (not acertou and not enforcou):
                try:
                    self.desenha_cabecalo()
                    letras_faltando = str(letras_acertadas.count('_'))

                    print("".join(letras_acertadas))
                    print(f'Falta acertar {letras_faltando} letras')
                    print(f'Tentativas restantes: {7-erros}')

                    chute_player_1 = self.__forca_1.pede_chute()
                    if chute_player_1 in palavra_secreta:
                        self.__forca_1.marca_letra_correta(chute_player_1, letras_acertadas, palavra_secreta)

                    else:
                        erros += 1
                        self.desenha_forca(erros)
                    enforcou = erros == len(palavra_secreta)
                    acertou = "_" not in letras_acertadas
                    print ("\n" * 130)
                except EOFError:
                    break
            if (acertou):
                print(f"Parabéns!! acertou todas as letras da palavra: {palavra_secreta}")
            elif (enforcou):
                print("perdeu")

        elif self.__modo == 'VS':


            #carrega dados jogador um
            self.__forca_1.escolhe_palavra()
            palavra_secreta_player_1 = self.__forca_1.visualisa_palavra()
            letras_acertadas_player_1 = self.__forca_1.display_palavra(palavra_secreta_player_1)
            erros_player_1 = 0
            letras_faltando_player_1 = len(letras_acertadas_player_1)
            acertou_player_1 = False
            enforcou_player_1 = False

            self.__forca_2.escolhe_palavra()
            palavra_secreta_player_2 = self.__forca_2.visualisa_palavra()
            letras_acertadas_player_2 = self.__forca_2.display_palavra(palavra_secreta_player_2)
            erros_player_2 = 0
            letras_faltando_player_2 = len(letras_acertadas_player_2)
            acertou_player_2 = False
            enforcou_player_2 = False

            while (not acertou_player_1 and not enforcou_player_1 or not acertou_player_2 and not enforcou_player_2):
                try:
                    self.desenha_cabecalo()
                    print("Vez do jogador 1")
                    letras_faltando_player_1 = str(letras_acertadas_player_1.count('_'))
                    print("".join(letras_acertadas_player_1))
                    print(f'Falta acertar {letras_faltando_player_1} letras')
                    print(f'Tentativas restantes: {7-erros_player_1}')

                    chute_player_1 = self.__forca_1.pede_chute()
                    if chute_player_1 in palavra_secreta_player_1:
                        self.__forca_1.marca_letra_correta(chute_player_1, letras_acertadas_player_1, palavra_secreta_player_1)

                    else:
                        erros_player_1 += 1
                        self.desenha_forca(erros_player_1)
                    enforcou_player_1 = erros_player_1 == len(palavra_secreta_player_1)
                    acertou_player_1 = "_" not in letras_acertadas_player_1


                    if (acertou_player_1):
                        print(f"Parabéns!! Jogador 1 acertou todas as letras da palavra: {palavra_secreta_player_1}")
                        break
                    elif (enforcou_player_1):
                        print("perdeu jogador 1")
                        break
                    print ("\n" * 130)
                    #==========================================================================================================
                    self.desenha_cabecalo()
                    print("Vez do jogador 2")
                    letras_faltando_player_2 = str(letras_acertadas_player_2.count('_'))
                    print("".join(letras_acertadas_player_2))
                    print(f'Falta acertar {letras_faltando_player_2} letras')
                    print(f'Tentativas restantes: {7-erros_player_2}')

                    chute_player_2 = self.__forca_2.pede_chute()
                    if chute_player_2 in palavra_secreta_player_2:
                        self.__forca_2.marca_letra_correta(chute_player_2, letras_acertadas_player_2, palavra_secreta_player_2)

                    else:
                        erros_player_2 += 1
                        self.desenha_forca(erros_player_2)
                    enforcou_player_2 = erros_player_2 == len(palavra_secreta_player_2)
                    acertou_player_2 = "_" not in letras_acertadas_player_2


                    if (acertou_player_2):
                        print(f"Parabéns!! Jogador 2 acertou todas as letras da palavra: {palavra_secreta_player_2}")
                        break
                    elif (enforcou_player_2):
                        print("perdeu jogador 2")
                        break
                except EOFError:
                    break
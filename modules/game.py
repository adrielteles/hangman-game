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
        
        espacamento = "*"*40
        print(f'{espacamento}\n JOGO DA FORCA MODO {self.__modo}\n{espacamento}')

    def play(self, modo: int):

        self.escolhe_modo(modo)
        if self.__modo == 'SOLO':
            self.__forca_1.escolhe_tema()
            self.__forca_1.escolhe_palavra()
            palavra_secreta = self.__forca_1.visualisa_palavra()
            letras_acertadas = self.__forca_1.display_palavra(palavra_secreta)
            
            print(palavra_secreta)
            print("".join(letras_acertadas))
            while True:
                try:
                    chute_player_1 = self.__forca_1.pede_chute()
                    if chute_player_1 in palavra_secreta:
                        self.__forca_1.marca_letra_correta(chute_player_1, letras_acertadas, self.__forca_1.visualisa_palavra())
                    print("".join(letras_acertadas))
                except EOFError:
                    break

        elif self.__modo == 'VS':

            self.__forca_1.escolhe_tema()
            self.__forca_2.escolhe_tema()


            self.__forca_1.escolhe_palavra()
            self.__forca_2.escolhe_palavra()
            while True:
                try:
                    print("Vez do jogador 1")
                    print(self.__forca_1.display_palavra())
                    chute_player_1 = self.__forca_1.pede_chute()
                    print(chute_player_1)
                    print("Vez do jogador 2")
                    print(self.__forca_2.display_palavra())
                    chute_player_2 = self.__forca_2.pede_chute()
                    print(chute_player_2)
                except EOFError:
                    break
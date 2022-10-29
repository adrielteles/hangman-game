import random 
from pathlib import Path
class Forca:

    def __init__(self) -> None:

            self.__palavra = []
            self.__dicas = []
            self.__temas = []

    #Methods

    def escolhe_palavra(self):

        lista_palavras = []
        lista_palavras_refeitas = []
        lista_palavra = []

        caminho = Path(f'./database/palavras/')
        for arquivos in caminho.iterdir():
            self.__temas.append(arquivos.name)
        arquivo = open(f'{caminho}/{self.__temas[random.randrange(0,len(self.__temas))]}', 'r')

        while True:
            linha = arquivo.readline()
            if (linha != ""):
                lista_palavras.append(linha)
            else:
                break
        arquivo.close()

        for item in lista_palavras:

            item_forca = item.split(', ')
            lista_palavras_refeitas.append([item_forca[0], item_forca[1],item_forca[2],item_forca[3],item_forca[4],item_forca[5][:-1]])
            lista_palavra.append(item_forca[0])

        random_choice = random.randrange(0, len(lista_palavra))

        for item in lista_palavras_refeitas:

            if item[0] == lista_palavra[random_choice]:

                self.__palavra.append(item[0])
                self.__dicas.append(item[1])
                self.__dicas.append(item[2])
                self.__dicas.append(item[3])
                self.__dicas.append(item[4])
                self.__dicas.append(item[5])
    
    def visualisa_palavra(self):
        return self.__palavra[-1]

    def visualisa_dica(self, num_dica:int):
        
        if num_dica <= len(self.__dicas):
            if num_dica == 1:
                return self.__dicas[0]
            if num_dica == 2:
                return self.__dicas[1]
            if num_dica == 3:
                return self.__dicas[2]
            if num_dica == 4:
                return self.__dicas[3]
            if num_dica == 5:
                return self.__dicas[4]
        else:
            print("Erro não existe essa dica!")

    def display_palavra(self, palavra):
        display_palavra = ""
        for letra in palavra:
            if letra == " ":
                display_palavra += "-"
            else:
                display_palavra += "_"
        return [letra for letra in display_palavra]

    def pede_chute(self):
        while True:
            try:
                chute = str(input("Qual seu chute?"))

                if len(chute) <= 1:
                    return chute
                else:
                    print("Chute invalido")
            except EOFError:
                break

    def marca_letra_correta(self, chute, letras_acertadas, palavra_secreta):

        index = 0
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[index] = letra
            index += 1





forcateste = Forca()
forcateste.escolhe_palavra()
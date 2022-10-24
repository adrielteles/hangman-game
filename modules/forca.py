import random 
class Forca:

    def __init__(self) -> None:

            self.__palavra = ""
            self.__dicas = []
            self.__modo = ""
            self.__tema = ""

    #Methods

    def escolhe_modo(self, modo:int):
        
        if modo == 1:
            self.__modo = "SOLO"
        if modo == 2:
            self.__modo = "VS"


    def ver_modo(self):
        return self.__modo

    def escolhe_tema(self):
        temas = ["carros"]
        self.__tema = temas[random.randrange(0,len(temas))]

        return self.__tema


    def desenha_cabecalo(self):
        
        espacamento = "*"*40
        print(f'{espacamento}\n JOGO DA FORCA MODO {self.__modo}\n{espacamento}')


    def escolhe_palavra(self):

        lista_palavras = []
        lista_palavras_refeitas = []
        lista_palavra = []

        arquivo = open(f'./database/palavras/{self.__tema}.txt', 'r')

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

                self.__palavra = item[0]
                self.__dicas.append(item[1])
                self.__dicas.append(item[2])
                self.__dicas.append(item[3])
                self.__dicas.append(item[4])
                self.__dicas.append(item[5])
    
    def visualisa_palavra(self):
        return self.__palavra

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

    def display_palavra(self):
        display_palavra = ""
        for letra in self.__palavra:
            if letra == " ":
                display_palavra += "-"
            else:
                display_palavra += "_"
        return display_palavra


    def pede_chute(self):
        while True:
            try:
                chute = str(input("Qual seu chute?"))

                if len(chute) <= 1:
                    return chute
            except:
                ("Chute invalido")




forcateste = Forca()
forcateste.escolhe_tema()
forcateste.escolhe_palavra()

print(forcateste.visualisa_palavra())
print(forcateste.visualisa_dica(1))
print(forcateste.visualisa_dica(2))
print(forcateste.visualisa_dica(3))
print(forcateste.visualisa_dica(4))
print(forcateste.visualisa_dica(5))



print(forcateste.display_palavra())



from pathlib import Path
import random
class Forca:

    def __init__(self) -> None:
        
        self.__palavra_secreta = ''
        self.__letras_acertadas = ''
        self.__letras_usadas = ''
        self.__tema = ''
        self.__temas = []
        self.__listaPalavras = []
        self.__pathdb = Path(f'./database/palavras')
        self.__erros = 0


    def getPalavraSecreta(self):
        return self.__palavra_secreta

    def getLetrasAcertadas(self):
        return self.__letras_acertadas

    def setRandomPalavraSecreta(self):

        arquivo = open(f'{self.__pathdb}/{self.__tema}.txt', 'r',encoding='utf-8')

        while True:
            line = arquivo.readline()
            if (line != ""):
                self.__listaPalavras.append(line.replace("\n", "").upper())
                continue
            break
        arquivo.close()
        self.__palavra_secreta = self.__listaPalavras[random.randrange(0, len(self.__listaPalavras))]
    

    def getTemas(self):
        return self.__temas

    def setTemas(self):

        for arquivos in self.__pathdb.iterdir():
            self.__temas.append(arquivos.name[:-4])
    
    def getTema(self):
        return self.__tema

    def setTema(self, tema:str):
        self.__tema = tema

    def setLetra(self, letra:str):
        if letra not in self.__letras_usadas:
            self.__letras_usadas += letra
            self.__letras_usadas += ' '
        if letra in self.__palavra_secreta:
            self.__letras_acertadas += letra
        elif letra not in self.__palavra_secreta:
            self.__erros += 1

    def getLetrasUsadas(self):
        return self.__letras_usadas

    def getErros(self):
        return self.__erros

    def formaPalavra(self):
        formaPalavra = ''
        for letra_secreta in self.__palavra_secreta:
            if letra_secreta in self.__letras_acertadas:
                formaPalavra += letra_secreta
            elif letra_secreta == " ":
                formaPalavra += "-"
            else:
                formaPalavra += '_'
        return formaPalavra

    def winner(self,tentativas:int):
        if self.formaPalavra().replace('-',' ') == self.__palavra_secreta and tentativas<8:
            return True
        elif tentativas >= 8:
            return False

    def desenhaforca(self, palavra:str, tentativa:int):
        if tentativa == 0:
            print(f"""
{'_'*10}
  |
  |
  |       
  |       
  |       
{'='*15}| {palavra}""")
        elif tentativa == 1:
            print(f"""
{'_'*10}
  |
  |   O
  |       
  |       
  |       
{'='*15}| {palavra}""")

        elif tentativa == 2:
            print(f"""
{'_'*10}
  |
  |   O
  |   |   
  |       
  |       
{'='*15}| {palavra}""")

        elif tentativa == 3:
            print(f"""
{'_'*10}
  |
  |   O
  |  /|   
  |       
  |       
{'='*15}| {palavra}""")

        elif tentativa == 4:
            print(f"""
{'_'*10}
  |
  |   O
  |  /|\   
  |       
  |       
{'='*15}| {palavra}""")

        elif tentativa == 5:
            print(f"""
{'_'*10}
  |
  |   O
  |  /|\   
  |   |   
  |       
{'='*15}| {palavra}""")

        elif tentativa == 6:
            print(f"""
{'_'*10}
  |
  |   O
  |  /|\   
  |   |   
  |  /    
{'='*15}| {palavra}""")

        elif tentativa == 7:
            print(f"""
{'_'*10}
  |
  |   O
  |  /|\   
  |   |   
  |  / \    
{'='*15}| {palavra}""")

        elif tentativa == 8:
            print(f"""
{'_'*10}
  |   |
  |   O
  |  /|\   
  |   |   
  |  / \    
{'='*15}| {palavra}""")
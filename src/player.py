from pathlib import Path
class Player:


    def __init__(self) -> None:
        
        self.__nome= ''
        self.__palavras_acertadas = 0
        self.__letras_acertadas = 0
        self.__exp = 0
        self.__level = 0
        self.__patente = ''
        self.__pathdb = Path(f'./database/players')

    @property
    def getNome(self):
        return self.__nome

    def setNome(self, nome:str):
        self.__nome = nome

    @property
    def getPalavrasAcertadas(self):
        return self.__palavras_acertadas

    def palavraAcertadas(self, numeroPalavras:int):
        self.__palavras_acertadas += numeroPalavras

    @property
    def getLetrasAcertadas(self):
        return self.__letras_acertadas

    def letrasAcertadas(self, numeroLetras:int):
        self.__letras_acertadas += numeroLetras

    @property
    def getExp(self):
        return self.__exp

    def calculaExp(self):
        self.__exp = (self.__palavras_acertadas * 5) + (self.__letras_acertadas *2)

    @property
    def getLevel(self):
        return self.__level

    def calculaLevel(self):
        
        if self.__exp < 100:
            self.__level = 0

        elif self.__exp < 200:
            self.__level = 1

        elif self.__exp < 300:
            self.__level = 2

        elif self.__exp < 400:
            self.__level = 3

        elif self.__exp < 500:
            self.__level = 4

        elif self.__exp < 600:
            self.__level = 5

        elif self.__exp < 700:
            self.__level = 6

        elif self.__exp < 800:
            self.__level = 7

        elif self.__exp < 900:
            self.__level = 8

        elif self.__exp < 1000:
            self.__level = 9

        elif self.__exp < 1100:
            self.__level = 10

        elif self.__exp < 1200:
            self.__level = 11

        elif self.__exp < 1300:
            self.__level = 12

        elif self.__exp < 1400:
            self.__level = 13

        elif self.__exp < 1500:
            self.__level = 14

        elif self.__exp < 1600:
            self.__level = 15

        elif self.__exp < 1700:
            self.__level = 16

        elif self.__exp < 1800:
            self.__level = 17

        elif self.__exp < 1900:
            self.__level = 18

        elif self.__exp < 2000:
            self.__level = 19
        
        elif self.__exp < 2100:
            self.__level = 20

        elif self.__exp < 2200:
            self.__level = 21

        elif self.__exp < 2300:
            self.__level = 22

        elif self.__exp < 2400:
            self.__level = 23

        elif self.__exp < 2500:
            self.__level = 24

        elif self.__exp < 2600:
            self.__level = 25

        elif self.__exp < 2700:
            self.__level = 26

        elif self.__exp < 2800:
            self.__level = 27

        elif self.__exp < 2900:
            self.__level = 28

        elif self.__exp < 3000:
            self.__level = 29

        elif self.__exp < 3100:
            self.__level = 30

        elif self.__exp < 3200:
            self.__level = 31

        elif self.__exp < 3300:
            self.__level = 32

        elif self.__exp < 3400:
            self.__level = 33

        elif self.__exp < 3500:
            self.__level = 34

        elif self.__exp < 3600:
            self.__level = 35

        elif self.__exp < 3700:
            self.__level = 36

        elif self.__exp < 3800:
            self.__level = 37

        elif self.__exp < 3900:
            self.__level = 38

        elif self.__exp < 4000:
            self.__level = 39

        elif self.__exp < 4100:
            self.__level = 40

        elif self.__exp < 4200:
            self.__level = 41

        elif self.__exp < 4300:
            self.__level = 42

        elif self.__exp < 4400:
            self.__level = 43

        elif self.__exp < 4500:
            self.__level = 44

        elif self.__exp < 4600:
            self.__level = 45

        elif self.__exp < 4700:
            self.__level = 46

        elif self.__exp < 4800:
            self.__level = 47

        elif self.__exp < 4900:
            self.__level = 48

        elif self.__exp < 5000:
            self.__level = 49
        
        elif self.__exp < 5100:
            self.__level = 50

        elif self.__exp < 5200:
            self.__level = 51

        elif self.__exp < 5300:
            self.__level = 52

        elif self.__exp < 5400:
            self.__level = 53

        elif self.__exp < 5500:
            self.__level = 54

        elif self.__exp < 5600:
            self.__level = 55

        elif self.__exp < 5700:
            self.__level = 56

        elif self.__exp < 5800:
            self.__level = 57

        elif self.__exp < 5900:
            self.__level = 58

        elif self.__exp < 6000:
            self.__level = 59
        else:
            self.__level = 60


    @property
    def getPatente(self):
        return self.__patente

    def calculaPatente(self):
        if self.__level < 10:
            self.__patente = 'Duck'
        elif self.__level < 20:
            self.__patente = 'Koala'
        elif self.__level < 30:
            self.__patente = 'Skunk'
        elif self.__level < 40:
            self.__patente = 'Cow'
        elif self.__level < 50:
            self.__patente = 'Panda'
        elif self.__level < 60:
            self.__patente = 'Unicorn'
        else:
            self.__patente = 'Dragon'
            
    def patenteIcon(self):
        if self.__patente == 'Duck':
            return '🦆'
        elif self.__patente == 'Koala':
            return '🐨'
        elif self.__patente == 'Skunk':
            return '🦨'
        elif self.__patente == 'Cow':
            return '🐮'
        elif self.__patente == 'Panda':
            return '🐼'
        elif self.__patente == 'Unicorn':
            return '🐨'
        elif self.__patente == 'Dragon':
            return '🐲'

    def procuraPlayer(self,nome:str):
        for arquivo in self.__pathdb.iterdir():
            if arquivo.name[:-4] == nome:
                arquivo = open(f'{self.__pathdb}/{nome}.txt', 'r',encoding='utf-8')
                player = arquivo.readline()
                arquivo.close()

                itens_player = player.split(',')
                self.__nome = itens_player[0]
                self.__palavras_acertadas = int(itens_player[1])
                self.__letras_acertadas = int(itens_player[2])
                self.__exp = int(itens_player[3])
                self.__level = int(itens_player[4])
                self.__patente = itens_player[5]
        self.__nome = nome

    def savePlayer(self):
        self.calculaExp()
        self.calculaLevel()
        self.calculaPatente()
        with open(f'{self.__pathdb}/{self.__nome}.txt', 'w',encoding='utf-8') as f:
            f.writelines(str(f'{self.__nome},{self.__palavras_acertadas},{self.__letras_acertadas},{self.__exp},{self.__level},{self.__patente}'))
            f.close()
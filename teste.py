from pathlib import Path, PurePosixPath, PureWindowsPath
import os

diretorio = Path.cwd()
print(diretorio)
# caminho = Path('database/palavras/')

#com parent

inicial = diretorio.parent

print(inicial)

# com caminho absoluto ==> '../'

absoluto = os.path.abspath('../')
print(absoluto)

# OUTPUT:
 
# D:\Projetos\hangman-game
# D:\Projetos
# D:\Projetos
# PS D:\Projetos\hangman-game> python .\teste.py
# D:\Projetos\hangman-game
# D:\Projetos
# D:\Projetos
# PS D:\Projetos\hangman-game> 


import pyautogui
import pandas as pd
import time

pyautogui.PAUSE = 1

# passo-1 abrir o navegador para entrar no sistema
pyautogui.press("win")

pyautogui.write("edge")

pyautogui.press("enter")

time.sleep(8)

pyautogui.write("http://www.sauer.pro.br/python/automacao/index.html")

pyautogui.press("enter")

# passo-2 fazer login no sistema
pyautogui.click(x = 591, y = 259)

pyautogui.write("admin")

pyautogui.press("tab")

pyautogui.write("admin")

pyautogui.press("tab")

pyautogui.press("enter")

# passo-3 importar banco de dados
tabela = pd.read_csv("alunos.csv")

time.sleep(8)

# passo-4 cadastrar os alunos
for linha in tabela.index:
    
    nome = tabela.loc[linha, "Nome"]
    
    email = tabela.loc[linha, "Email"]
    
    endereco = tabela.loc[linha, "Endereco"]
    
    telefone = tabela.loc[linha, "Telefone"]
    
    pyautogui.click(x = 493, y = 330)

    pyautogui.write(str(nome))

    pyautogui.press("tab")

    pyautogui.write(str(email))

    pyautogui.press("tab")

    pyautogui.write(str(endereco))

    pyautogui.press("tab")

    pyautogui.write(str(telefone))

    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)
    

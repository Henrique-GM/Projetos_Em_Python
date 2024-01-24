import pyautogui
import pandas as pd
import time

# importar a base de produtos
tabela = pd.read_csv("produtos.csv")


# define o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.5

# Abrir sistemas (no nosso caso o chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.position(x=441, y=60)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# esperar carregar
time.sleep(5)

# Fazer loguin (aqui pode preencher com qualquer dado de loguin)
pyautogui.click(x=476, y=402)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")

# Aqui precisamos percorrer as linhas da tabela
# para cada linha vamos cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=480, y=290) # clica no 1 campo
    # codigo
    pyautogui.write(str(tabela.loc[linha, "codigo"])) # pega o código da tabela e escreve no campo
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab") # passa para o proximo campo
    # agora repeti isso para os outros campos
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    if not pd.isna(tabela.loc[linha, "obs"]): # verifica se existe alguma informação em obs, caso contrario não preenche
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    # ele não pode ir até o final da tela para o click da linha de baixo funcionar sempre
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.scroll(5000)

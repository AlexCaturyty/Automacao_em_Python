# Lógica

# Passo 1: Fazer login

import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link) 
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=706, y=379)
pyautogui.write("AlexDev")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.click(x=668, y=557)

time.sleep(2)

# Passo 2: Importar os dados 
import pandas

tableProducts = pandas.read_csv("produtos.csv")
print(tableProducts)

for linha in tableProducts.index:

    # Passo 3: Cadastrar um produto 
    pyautogui.click(x=600, y=300)

    codigo = tableProducts.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tableProducts.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = tableProducts.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = tableProducts.loc[linha, "categoria"]
    pyautogui.write(str(categoria))    
    pyautogui.press("tab")

    preco_unitario = tableProducts.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    custo  = tableProducts.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tableProducts.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)



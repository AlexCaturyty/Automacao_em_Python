# Automação em Python com PyAutoGUI e Pandas

## Descrição do Projeto

Nesta aplicação, desenvolvi uma automação utilizando Python, PyAutoGUI e Pandas para cadastrar produtos diretamente a partir de um arquivo CSV que contém os dados de cada produto.

## Código Exemplo

A seguir, um trecho do código em Python que ilustra a lógica utilizada na automação:

```python
# Importando bibliotecas necessárias
import pandas as pd
import pyautogui
import time

# Carregando dados do arquivo CSV
dados_produtos = pd.read_csv("arquivo_produtos.csv")

# Iterando sobre os dados para realizar a automação
for index, produto in dados_produtos.iterrows():
    # Simulando cliques e preenchimento de campos com PyAutoGUI
    pyautogui.click(100, 200)  # Exemplo de coordenadas, ajuste conforme necessário
    pyautogui.write(produto["Nome"])
    pyautogui.write(produto["Preço"])
    pyautogui.click(200, 300)  # Exemplo de coordenadas, ajuste conforme necessário
    
    # Aguardando um breve momento antes de cada ação
    time.sleep(1)

# Fim do exemplo

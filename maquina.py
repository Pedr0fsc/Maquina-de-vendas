# Implemente uma máquina de venda de bebidas em Python, de acordo com os requisitos abaixo

"""ID Produto Valor Estoque
1 Coca-cola |R$ 3,75| 2
2 Pepsi |R$ 3,67| 5
3 Monster |R$ 9,96| 1
4 Café |R$ 1,25| 100
5 Redbull |R$ 13,99| 2
Atividade somativa
"""
# matriz que corrresponde aos valores determinados pelo pro
matriz = [[1, 3.75,  2],
          [2, 3.67,  5],
          [3, 9.96,  1],
          [4, 1.25,  100],
          [5, 13.99, 2]]
# relaciona os produtos com o Id correspondente
nome_produtos = {
    1: "Coca-Cola",
    2: "Pepsi",
    3: "Monster",
    4: "Café",
    5: "Redbull"
}

print('''Selecione abaixo o Id correspondente a bebida que deseja comprar:
     [1] Coca-cola
     [2] Pepsi
     [3] Monster
     [4] Café
     [5] Redbull''')

while True: # criado para ficar em loop até a pessoa escolher um Id válido a bebida
    id_digitado = int(input('Insira o valor do Id desejado:'))
    if 0 < id_digitado < 6:
        break
    else:
        continue
    
produto_encontrado = None
for linha in matriz:
    if linha[0] == id_digitado:
        produto_encontrado = linha
        break

if produto_encontrado:
    nome = nome_produtos[produto_encontrado[0]] # oie
    valor = produto_encontrado[1]
    estoque = produto_encontrado[2]
    
    print(f"ID: {id_digitado} | Nome: {nome} | Valor: R${valor} | Estoque: {estoque}") # adorei ficar observando só kkkkkkkkkkkkkkkk          vai programar todo o resto agr kkkkkkkk

while True:
    valor_inserido = int(input('Insira o valor colocado na máquina: '))
    if valor_inserido >= valor:
        print(f"Você vai pagar R${valor_inserido}")
        break
    else:
        print("Valor abaixo do requisitado, insira um valor válido!")
        continue
    
moedas = [[0.05,0.10,0.25,0.5,1],
          2,5,10,20,50,100]

estoque -= 1

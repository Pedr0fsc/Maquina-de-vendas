# Implemente uma máquina de venda de bebidas em Python, de acordo com os requisitos abaixo

"""ID Produto Valor Estoque
1 Coca-cola |R$ 3,75| 2
2 Pepsi |R$ 3,67| 5
3 Monster |R$ 9,96| 1
4 Café |R$ 1,25| 100
5 Redbull |R$ 13,99| 2
Atividade somativa
"""
while True:
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
    modo = int(input('''Insira o modo que vai ser iniciado, caso selecione o modo administrador será solicitado uma senha.
                         Opcões:
                         [1] Visitante
                         [2] Administrador'''))# responsável por pergutar se a pessoa vai querer o modo visitante ou adm
    def modo_admin():# sistema criado para solicitar senha e evitar que qualquer pessoa aceite
        senha = input("Digite a senha para entrar no modo administrador: ")
        if senha != "adm2415":
            print("Senha inválida!")
            return
        print("""Selecione o modo que deseja operar:
              [1] Cadastrar
              [2] Editar
              [3] Remover""")
        operacao = int(input('Insira o modo que deseja operar:'))
        if operacao == 1:# vai ser reponsável por cadastrar novos produtos
            produto_novo = input('Digite o nome da nova bebida que vai pertencer a máquina: ')
            id_novo = int(input('Insira o novo ID: '))
            estoque_novo = int(input('Insira o valor do estoque novo: '))
            preco_novo = float(input('Insira o valor do novo produto: '))
            nome_produtos[id_novo] = produto_novo
            matriz.append([id_novo,preco_novo,estoque_novo])
        elif operacao == 2:# vai ser responsável por editar os produtos
            id_editar = int(input('Insira o valor do ID do produto que deseja editar: '))
            for linha in matriz():
                if linha[0] == id_editar:
                    novo_nome = str(input('Insira o novo nome do produto: '))
                    novo_preco = float(input('Insira o novo valor do preço: '))
                    novo_estoque = int(input('Insira a nova quantidade de estoque: '))
                    matriz[linha][2] = novo_preco
                    matriz[linha][3] = novo_estoque
                    nome_produtos[id_novo] = novo_nome
                print('Produto atualizado!')
        elif operacao == 3:# vai ser responsável por remover o estoque
            id_remover = int(input('Insira o valor do Id que deseja remover: '))
            for linha in matriz:
                if linha[0] == id_remover:
                    del matriz[linha]
            nome_produtos.pop(id_remover, None)
        else:
            print('Opção inválida')
    if modo == 2:
            modo_admin()
    elif modo == 1:
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
                print(f"Você vai pagar R${valor}")
                break
            else:
                print("Valor abaixo do requisitado, insira um valor válido!")
                continue
    # começar a colocar o estoque    
    # vai determinar o estoque de moedas que vai ter disponível
        estoqueTroco = [[100.0, 5],
                        [50.0,15],
                        [20.0,22],
                        [10.0,17],
                        [5.0,22],
                        [2.0,26],
                        [1.0,35],
                        [0.5,49],
                        [0.25,50],
                        [0.1,61],
                        [0.05,37]]
        def calcularTroco(valor, valor_inserido):
                troco = (valor_inserido - valor) # resposável por calcular o troco
                trocoUsado = []
                for moeda in sorted(estoqueTroco.keys(), reverse=True): # vai começar procurando as moedas e notas maiores
                    quantidadeNecessaria = int(troco // moeda) # vai procurar a quantidade de moeda 
                    quantidadeUsada = min(quantidadeNecessaria, troco[moeda]) # essa parte vai calcular o troco usando a menor quantidade de moedas possível
                    if quantidadeUsada > 0:
                        trocoUsado[moeda] = quantidadeUsada
                        troco -= (quantidadeUsada * moeda)
                        if troco > 0:
                            return None
                        else:
                            for moeda, qtd in trocoUsado.itens():
                                matriz[moeda][1] -= qtd
                                return trocoUsado
    else:
        print('Opcão inválida tente novamente!')

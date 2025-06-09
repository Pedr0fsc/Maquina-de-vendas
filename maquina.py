matriz = [[1, 3.75,  2],  # Matriz com o ID, preços e quantidades de produtos
          [2, 3.67,  5],
          [3, 9.96,  1],
          [4, 1.25,  100],
          [5, 13.99, 2]]

nome_produtos = {  # Dicionário com os produtos da máquina
    1: "Coca-Cola",
    2: "Pepsi",
    3: "Monster",
    4: "Café",
    5: "Redbull"
}

estoqueTroco = {  # Dicionário com o troco disponível 
    100.0: 5, # 100 reais
    50.0: 15, # 50 reais
    20.0: 22, # 20 reais
    10.0: 17, # 10 reais
    5.0: 22, # 5 reais
    2.0: 26, # 2 reais
    1.0: 35, # 1 real
    0.5: 49, # 50 centavos
    0.25: 50, # 25 centavos
    0.1: 61, # 10 centavos
    0.05: 37, # 5 centavos
    0.01: 92 # 1 centavo
}

def calcularTroco(valor, valor_inserido): # Função para calcular o troco
    troco = round((valor_inserido - valor) * 100) # Cálculo do troco
    troco_usado = {} # Dicionário para guardar as moedas usados no troco
    for moeda in sorted(estoqueTroco.keys(), reverse=True):  # Ordenar os valores do maior para o menor
        moeda_centavos = int(round(moeda * 100)) # Converte os valores float dos centavos para um valor inteiro
        quantidade_necessaria = int(troco // moeda_centavos) 
        quantidade_usada = min(quantidade_necessaria, estoqueTroco[moeda]) # Pega o mínimo entre o necessário e o troco
        if quantidade_usada > 0:
            troco_usado[moeda] = quantidade_usada
            troco -= quantidade_usada * moeda_centavos # Diminui o troco restante
    if troco > 0:
        return None
    for moeda, qtd in troco_usado.items():
        estoqueTroco[moeda] -= qtd
    return troco_usado

def gerar_novo_id():  
    if not matriz:
        return 1
    return max(linha[0] for linha in matriz) + 1

def reordenar_ids():
    global matriz, nome_produtos
    nova_matriz = []
    novo_nome_produtos = {}
    
    for novo_id, linha in enumerate(sorted(matriz, key=lambda x: x[0]), start=1):
        _, preco, estoque = linha
        nova_matriz.append([novo_id, preco, estoque])
        nome = nome_produtos.get(linha[0], "Desconhecido")
        novo_nome_produtos[novo_id] = nome

    matriz = nova_matriz
    nome_produtos = novo_nome_produtos

def modo_admin(): # Permite que o administrador gerencie os produtos
    senha = input("Digite a senha para entrar no modo administrador: ")
    if senha != "adm2415":
        print("Senha inválida!")
        return
    
    while True:
        print("""Selecione o modo que deseja operar:
            [1] Cadastrar
            [2] Editar
            [3] Remover
            [4] Sair""")
        try:
            operacao = int(input("Escolha a operação: "))
        except ValueError:
            print("Opção inválida.")
            continue
        
        if operacao == 1: # Operação de cadastro de produtos
            for linha in matriz:
                    id_produto = linha[0]
                    nome = nome_produtos.get(id_produto, "Nome desconhecido")
                    preco = linha[1]
                    estoque = linha[2]
                    print(f"[{id_produto}] {nome} - R${preco:.2f} | {estoque} unidade(s)")
            
            produto_novo = input('Digite o nome da nova bebida: ')
            id_novo = gerar_novo_id()
            
            try:
                preco_novo = float(input('Insira o preço do novo produto: '))
            except ValueError:
                print("Valor monetário inválido. Use apenas números.")
                continue
            
            try:
                estoque_novo = int(input('Insira o estoque inicial: '))
            except ValueError:
                print("Número de estoque inválido. Use apenas números.")
                continue
            
            nome_produtos[id_novo] = produto_novo
            matriz.append([id_novo, preco_novo, estoque_novo])
            
        elif operacao == 2: # Operação de edição de produtos
            if not matriz:
                print("Nenhum produto cadastrado.")
                continue

            print("\n--- Lista de produtos ---")
            for linha in matriz:
                id_prod, preco, qtd = linha
                print(f"[{id_prod}] {nome_produtos[id_prod]} - R${preco:.2f} | Estoque: {qtd}")

            while True:
                try:
                    id_editar = int(input("Digite o ID do produto que deseja editar (ou -1 para voltar): "))
                except ValueError:
                    print("ID inválido. Use apenas números.")
                    continue

                if id_editar == -1:
                    break

                encontrado = False
                for i, (pid, _, _) in enumerate(matriz):
                    if pid == id_editar:
                        encontrado = True
                        while True:
                            print(f"\n--- Editar produto: {nome_produtos[pid]} ---")
                            print("[1] Editar nome")
                            print("[2] Editar preço")
                            print("[3] Editar estoque")
                            print("[0] Voltar")
                            try:
                                opcao_edicao = int(input("Escolha a opção: "))
                            except ValueError:
                                print("Opção inválida. Use apenas números.")
                                continue

                            if opcao_edicao == 1:
                                novo_nome = input("Novo nome do produto: ").strip()
                                if novo_nome:
                                    nome_produtos[pid] = novo_nome
                                    print("Nome atualizado!")
                                else:
                                    print("Nome não alterado.")
                            elif opcao_edicao == 2:
                                print(f"Preço atual: {matriz[i][1]}")
                                try:
                                    novo_preco = float(input("Novo preço do produto: "))
                                    matriz[i][1] = novo_preco
                                    print("Preço atualizado!")
                                except ValueError:
                                    print("Preço inválido.")
                            elif opcao_edicao == 3:
                                print(f"Estoque atual: {matriz[i][2]}")
                                try:
                                    novo_estoque = int(input("Novo estoque do produto: "))
                                    matriz[i][2] = novo_estoque
                                    print("Estoque atualizado!")
                                except ValueError:
                                    print("Estoque inválido.")
                            elif opcao_edicao == 0:
                                print("Voltando ao menu de edição de produtos...\n")
                                break
                            else:
                                print("Opção inválida.")
                        break
                if not encontrado:
                    print("Produto com esse ID não encontrado. Tente novamente.")

        elif operacao == 3: # Operação de remoção de produtos
            for linha in matriz:
                    id_produto = linha[0]
                    nome = nome_produtos.get(id_produto, "Nome desconhecido")
                    preco = linha[1]
                    estoque = linha[2]
                    print(f"[{id_produto}] {nome} - R${preco:.2f} | {estoque} unidade(s)")
            
            try:
                id_remover = int(input('ID do produto a ser removido: '))
            except ValueError:
                print("ID inválido. Use apenas números.")
                continue
            
            for i, linha in enumerate(matriz):
                if linha[0] == id_remover:
                    del matriz[i]
                    nome_produtos.pop(id_remover, None)
                    print("Produto removido.")
                    reordenar_ids()
                    break
            else:
                print("Produto não encontrado.")
                
        elif operacao == 4: # Operação de saída do modo administrador
            print("Saindo do modo administrador...\n")
            break
        else:
            print("Opção inválida.")

compras_realizadas = [] # Array com um resumo da compra feita, para emitir uma nota fiscal

while True:
    try:
        modo = int(input('''Insira o modo:
                            [1] Visitante
                            [2] Administrador
                            [3] Sair
                            Sua opção: '''))
        
        if modo == 2: # Operação que chama a função modo_admin()
            modo_admin()

        elif modo == 1: # Operação de compra para os clientes
            modo_visitante_ativo = True
            while modo_visitante_ativo:
                print("\n--- Lista de Produtos ---")
                for linha in matriz:
                    id_produto = linha[0]
                    nome = nome_produtos.get(id_produto, "Nome desconhecido")
                    preco = linha[1]
                    print(f"[{id_produto}] {nome} - R${preco:.2f}")

                while True:
                    try:
                        id_digitado = int(input("ID desejado: "))
                    except ValueError:
                        print("Digite um número válido.")
                        continue

                    produto_encontrado = None
                    for linha in matriz:
                        if linha[0] == id_digitado:
                            produto_encontrado = linha
                            break
                    if produto_encontrado:
                        break
                    else:
                        print("Produto não encontrado. Selecione um ID válido.")

                nome = nome_produtos[produto_encontrado[0]]
                valor = produto_encontrado[1]
                estoque = produto_encontrado[2]

                print(f"Produto: {nome} | Preço: R${valor:.2f} | Estoque: {estoque}")

                while True:
                    try:
                        valor_inserido = float(input('Insira o valor inserido na máquina: '))
                    except ValueError:
                        print("Valor inválido.")
                        continue

                    if valor_inserido >= valor:
                        print(f"Você vai pagar R${valor:.2f}")
                        troco = calcularTroco(valor, valor_inserido)
                        if troco is None:
                            print("Não há troco suficiente na máquina. Compra cancelada.")
                        else:
                            print("Troco: ")
                            for moeda, qtd in troco.items():
                                print(f"R${moeda:.2f} x {qtd}")
                            produto_encontrado[2] -= 1  # Atualiza o estoque
                            compras_realizadas.append({
                                "produto": nome,
                                "valor_pago": valor_inserido,
                                "preco": valor,
                                "troco": troco
                            })

                        while True:
                            try:
                                continuar = int(input("""Deseja continuar compra?
                                                        [1] Continuar
                                                        [2] Sair
                                                        R: """))
                                if continuar == 1:
                                    break  # Volta ao início do modo visitante
                                elif continuar == 2:
                                    print("Saindo do modo de compra...\n")
                                    modo_visitante_ativo = False
                                    break
                                else:
                                    print("Opção inválida.")
                            except ValueError:
                                print("Digite apenas 1 ou 2.")
                        break  # Sai do loop de pagamento
                    else:
                        print("Valor insuficiente. Insira um valor maior.")

        elif modo == 3: # Operação de finalização do sistema
            if compras_realizadas: # Caso o usuário tenha comprado algo -> Emissão de nota fiscal
                print("\n========== NOTA FISCAL ==========")
                total = 0
                for i, compra in enumerate(compras_realizadas, start=1):
                    print(f"\nCompra #{i}")
                    print(f"Produto: {compra['produto']}")
                    print(f"Preço: R${compra['preco']:.2f}")
                    print(f"Valor pago: R${compra['valor_pago']:.2f}")
                    print("Troco:")
                    for moeda, qtd in compra['troco'].items():
                        print(f"  R${moeda:.2f} x {qtd}")
                    total += compra['preco']
                print(f"\nTOTAL GASTO: R${total:.2f}")
                print("=================================\n")
            else: # Caso o usuário não tenha comprado nada -> Nenhuma compra realizada
                print("Nenhuma compra realizada.\n")
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
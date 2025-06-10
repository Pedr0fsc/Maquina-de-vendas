matriz = [[1, 3.75, 2],  # Matriz com o ID, preços e quantidades de produtos
          [2, 3.67, 5],
          [3, 9.96, 1],
          [4, 1.25, 100],
          [5, 13.99, 2]]

nome_produtos = {  # Dicionário com que relaciona ID aos produtos da máquina
    1: "Coca-Cola",
    2: "Pepsi",
    3: "Monster",
    4: "Café",
    5: "Redbull"
}

estoqueTroco = {  # Dicionário com o troco disponível
    100.0: 5,  # 100 reais
    50.0: 15,  # 50 reais
    20.0: 22,  # 20 reais
    10.0: 17,  # 10 reais
    5.0: 22,  # 5 reais
    2.0: 26,  # 2 reais
    1.0: 35,  # 1 real
    0.5: 49,  # 50 centavos
    0.25: 50,  # 25 centavos
    0.1: 61,  # 10 centavos
    0.05: 37,  # 5 centavos
    0.01: 92  # 1 centavo
}


def calcularTroco(valor, valor_inserido):  # Função para calcular o troco
    troco = round((valor_inserido - valor) * 100)  # Cálculo do troco em centavos e arredonda
    troco_usado = {}  # Dicionário para guardar as cédulas/moedas usadas no troco
    for moeda in sorted(estoqueTroco.keys(), reverse=True):  # Loop que percorre as moedas/cédulas do maior para o menor
        moeda_centavos = int(round(moeda * 100))  # Converte o valor da moeda para centavos
        quantidade_necessaria = int(troco // moeda_centavos)  # Calcula a quantidade necessária de tal moeda
        quantidade_usada = min(quantidade_necessaria,
                               estoqueTroco[moeda])  # Verifica se há o suficiente dessa moeda no estoque
        if quantidade_usada > 0:  # Se foi usado troco
            troco_usado[moeda] = quantidade_usada  # Registra essas moedas usadas para o troco
            troco -= quantidade_usada * moeda_centavos  # Diminui o troco restante que falta devolver
    if troco > 0:  # O troco não foi exato, não a moedas suficientes no estoque da máquina
        return None  # Cancela a compra
    for moeda, qtd in troco_usado.items():  # Atualiza o estoque do troco diminuindo as moedas usadas
        estoqueTroco[moeda] -= qtd
    return troco_usado  # Retorna as moedas usadas


def gerar_novo_id():  # Repondo estoque e organizando IDs
    if not matriz:  # Se o estoque estiver vazio
        return 1  # O produto adicionado terá como ID o número 1
    return max(linha[0] for linha in matriz) + 1  # Se estiver com produtos, pega o maior ID e soma mais 1


def reordenar_ids():  # Reodenação de IDs após a remoção de produtos
    global matriz, nome_produtos  # Trazendo funções globais para dentro da função
    nova_matriz = []  # Matriz com os produtos organizados
    novo_nome_produtos = {}  # Novo dicionário com os nomes atualizados

    for novo_id, linha in enumerate(sorted(matriz, key=lambda x: x[0]),
                                    start=1):  # Percorre a matriz ordenada pelo ID original, começando com novo_id = 1
        _, preco, estoque = linha
        # Adiciona na nova matriz o ID novo dos produtos, preço e estoque
        nova_matriz.append([novo_id, preco, estoque])
        nome = nome_produtos.get(linha[0],
                                 "Desconhecido")  # Atualiza o nome do produto para o novo ID usando o nome antigo
        novo_nome_produtos[novo_id] = nome
    # Atualização das variáveis globais utilizando as locais
    matriz = nova_matriz
    nome_produtos = novo_nome_produtos


def modo_admin():  # Permite que o administrador gerencie os produtos
    senha = input("Digite a senha para entrar no modo administrador: ")  # Pede a senha
    if senha != "adm2415":  # Verifica se tá correta
        print("Senha inválida!")
        return  # Saí da função se estiver errada

    while True:  # Caso a senha for verdadeira
        # Menu do Administrador
        print("""Selecione o modo que deseja operar:   
            [1] Cadastrar
            [2] Editar
            [3] Remover
            [4] Sair""")
        try:  # Pergunta até que o modo selecionado esteja dentre as opções listadas
            operacao = int(input("Escolha a operação: "))  # Lê a opção escolhida
        except ValueError:  # Verifica se a entrada está correta
            print("Opção inválida.")
            continue

        if operacao == 1:  # Cadastro de novos produtos
            for linha in matriz:  # Percorre toda a matriz, exibindo a no final como uma tabela
                id_produto = linha[0]
                nome = nome_produtos.get(id_produto, "Nome desconhecido")
                preco = linha[1]
                estoque = linha[2]
                print(f"[{id_produto}] {nome} - R${preco:.2f} | {estoque} unidade(s)")

            produto_novo = input('Digite o nome da nova bebida: ')  # Pede o nome de um novo produto
            id_novo = gerar_novo_id()  # Chama a função que adiciona um novo ID

            try:  # solicita o preço do novo produto e o valida
                preco_novo = float(input('Insira o preço do novo produto: '))  # Solicita um novo preço
            except ValueError:  # Verifica se o valor da entrada é realmente um float
                print("Valor monetário inválido. Use apenas números.")
                continue

            try:  # Solicita um estoque inicial e o valida
                estoque_novo = int(input('Insira o estoque inicial: '))
            except ValueError:  # Verifica se a entrada foi realmente um valor int
                print("Número de estoque inválido. Use apenas números.")
                continue

            nome_produtos[id_novo] = produto_novo  # Adiciona o novo produto ao dicionário
            matriz.append([id_novo, preco_novo, estoque_novo])  # Adiciona o novo produto a matriz

        elif operacao == 2:  # Operação de edição de produtos
            if not matriz:  # Caso o estoque esteja zerado
                print("Nenhum produto cadastrado.")
                continue

            print("\n--- Lista de produtos ---")
            for linha in matriz:  # Exibe uma tabela com ID, nome do produto, valor e quantidade
                id_prod, preco, qtd = linha
                print(f"[{id_prod}] {nome_produtos[id_prod]} - R${preco:.2f} | Estoque: {qtd}")

            while True:
                try:  # Escolha do produto que deseja editar e validação
                    id_editar = int(input("Digite o ID do produto que deseja editar (ou -1 para voltar): "))
                except ValueError:
                    print("ID inválido. Use apenas números.")
                    continue

                if id_editar == -1:  # -1 para finalizar essa operação e voltar ao menu anterior
                    break

                encontrado = False
                for i, (pid, _, _) in enumerate(matriz):
                    if pid == id_editar:
                        encontrado = True
                        while True:
                            # Menu para editar nome, preço ou estoque do produto selecionada
                            print(f"\n--- Editar produto: {nome_produtos[pid]} ---")
                            print("[1] Editar nome")
                            print("[2] Editar preço")
                            print("[3] Editar estoque")
                            print("[0] Voltar")
                            try:  # escolha da edição e validação
                                opcao_edicao = int(input("Escolha a opção: "))
                            except ValueError:
                                print("Opção inválida. Use apenas números.")
                                continue

                            if opcao_edicao == 1:  # Edição do nome
                                novo_nome = input("Novo nome do produto: ").strip()  # Solicita um novo nome
                                if novo_nome:
                                    nome_produtos[
                                        pid] = novo_nome  # Atualiza o dicionário adicionando o novo nome com o pid (id do produto)
                                    print("Nome atualizado!")
                                else:  # Caso nada seja escrito
                                    print("Nome não alterado.")
                            elif opcao_edicao == 2:  # Edição do preço
                                print(f"Preço atual: {matriz[i][1]}")  # Mostra o preço atual
                                try:  # Novo preço e validação
                                    novo_preco = float(input("Novo preço do produto: "))  # Entrada com o novo preço
                                    matriz[i][1] = novo_preco  # Insere na matriz, na coluna1(que corresponde ao preços)
                                    print("Preço atualizado!")
                                except ValueError:  # Validação
                                    print("Preço inválido.")
                            elif opcao_edicao == 3:  # Editar estoque
                                print(f"Estoque atual: {matriz[i][2]}")  # Mostra o estoque atual
                                try:
                                    novo_estoque = int(input("Novo estoque do produto: "))  # Solicita um novo estoque
                                    matriz[i][
                                        2] = novo_estoque  # Insere na matriz, na coluna2 (que corresponde ao estoque)
                                    print("Estoque atualizado!")
                                except ValueError:  # Validação
                                    print("Estoque inválido.")
                            elif opcao_edicao == 0:  # Sai da janela de edição dos produtos
                                print("Voltando ao menu de edição de produtos...\n")
                                break
                            else:  # Verificação se a opção escolhida está correta
                                print("Opção inválida.")
                        break
                if not encontrado:  # Verifica se o ID informado é válido
                    print("Produto com esse ID não encontrado. Tente novamente.")

        elif operacao == 3:  # Operação de remoção de produtos
            for linha in matriz:  # Exibe uma tabela com ID, nome do produto, valor e quantidade em estoque
                id_produto = linha[0]
                nome = nome_produtos.get(id_produto, "Nome desconhecido")
                preco = linha[1]
                estoque = linha[2]
                print(f"[{id_produto}] {nome} - R${preco:.2f} | {estoque} unidade(s)")

            try:  # Identificação do produto que será removido
                id_remover = int(input('ID do produto a ser removido: '))  # Entrada do ID do produto que será removido
            except ValueError:  # Verificação
                print("ID inválido. Use apenas números.")
                continue

            for i, linha in enumerate(matriz):  # Vai percorrer cada linha da matriz
                if linha[0] == id_remover:  # Verifica se o indíce da linha é igual ao escolhido pelo usuário
                    del matriz[i]
                    nome_produtos.pop(id_remover, None)  # Remove o produto do dicionário
                    print("Produto removido.")
                    reordenar_ids()  # Chama a função de reordenar os produtos
                    break
            else:  # Caso não encontre o produto
                print("Produto não encontrado.")

        elif operacao == 4:  # Operação de saída do modo administrador
            print("Saindo do modo administrador...\n")
            break
        else:  # Verificação do opção escolhida
            print("Opção inválida.")


compras_realizadas = []  # Array com um resumo da compra feita, para emitir uma nota fiscal

while True:  # Menu Principal
    try:
        modo = int(input('''Insira o modo:
                            [1] Visitante
                            [2] Administrador
                            [3] Sair
                            Sua opção: '''))

        if modo == 2:  # Operação que chama a função modo_admin()
            modo_admin()

        elif modo == 1:  # Operação de compra para os clientes
            modo_visitante_ativo = True
            while modo_visitante_ativo:
                print("\n--- Lista de Produtos ---")
                # Exibe uma tabela com o ID, nome e preço dos produtos
                for linha in matriz:
                    id_produto = linha[0]
                    nome = nome_produtos.get(id_produto, "Nome desconhecido")
                    preco = linha[1]
                    print(f"[{id_produto}] {nome} - R${preco:.2f}")

                while True:
                    try:  # Entrada do ID do produto escolhido pelo usuário e validação
                        id_digitado = int(input("ID desejado: "))
                    except ValueError:
                        print("Digite um número válido.")
                        continue

                    produto_encontrado = None  # Variável que armazena o produto (a linha do produto)
                    for linha in matriz:  # loop que percorre a matriz verificando se há o ID indicado
                        if linha[0] == id_digitado:
                            produto_encontrado = linha  # produto encontrado, encerra o for
                            break
                    if produto_encontrado:
                        break  # produto encontrado encerra o while de entrada do usuário
                    else:  # Erro, a máquina continua perguntando o produto ao usuário
                        print("Produto não encontrado. Selecione um ID válido.")

                nome = nome_produtos[
                    produto_encontrado[0]]  # vaeiavel que armazena o nome do produto com base no dicionário
                valor = produto_encontrado[1]  # variavel que mostra o valor do produto
                estoque = produto_encontrado[2]  # variavel que mostra quanto há em estoque desse produto

                print(
                    f"Produto: {nome} | Preço: R${valor:.2f} | Estoque: {estoque}")  # mostra ao consumidor um resumo da sua compra

                while True:  # Loop de pagamento
                    try:  # Solicita o valor a ser pago pelo usuário
                        valor_inserido = float(input('Insira o valor inserido na máquina: '))
                    except ValueError:  # Verifica se o valor foi inserido de fato
                        print("Valor inválido.")
                        continue

                    if valor_inserido >= valor:  # Verifica se o valor é suficiente para a compra
                        print(f"Você vai pagar R${valor:.2f}")  # Exibe o valor do produto
                        troco = calcularTroco(valor, valor_inserido)  # variável chama a função do calcúlo do troco
                        if troco is None:  # Valor inserido maior que o estoque de notas da máquina (compra cancela)
                            print("Não há troco suficiente na máquina. Compra cancelada.")
                        else:
                            print("Troco: ")
                            for moeda, qtd in troco.items():  # loop que percorre o dicionário de trocos
                                print(
                                    f"R${moeda:.2f} x {qtd}")  # Exibe a quantidade de cada moeda/cédula do troco do usuário
                            produto_encontrado[2] -= 1  # Atualiza o estoque
                            compras_realizadas.append({
                                "produto": nome,
                                "valor_pago": valor_inserido,
                                "preco": valor,
                                "troco": troco
                            })

                        while True:  # loop para perguntar ao usuário se ele deseja contiuar comprando
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
                    else:  # valor iserido insuficiente para a execução da compra
                        print("Valor insuficiente. Insira um valor maior.")

        elif modo == 3:  # Operação de finalização do sistema
            if compras_realizadas:  # Caso o usuário tenha comprado algo -> Emissão de nota fiscal
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
            else:  # Caso o usuário não tenha comprado nada -> Nenhuma compra realizada
                print("Nenhuma compra realizada.\n")
            print("Encerrando o programa.")
            break

        else:  # Nenhum modo do menu principal foi escolhido
            print("Opção inválida.")

    except Exception as e:  # Se a máquina dê qualquer erro não reconhecido pelas funções anteriores, mostrará aqui
        print(f"Ocorreu um erro: {e}")
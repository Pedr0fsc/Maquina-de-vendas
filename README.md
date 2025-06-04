# 🥤 Máquina de Vendas

Uma **máquina de vendas de bebidas** desenvolvida em **Python**, simulando o funcionamento de uma vending machine. O cliente pode escolher um produto, pagar com cédulas/moedas em reais e receber o troco calculado automaticamente.

---

## Descrição do Projeto

Este projeto tem como objetivo criar uma simulação funcional de uma **máquina de venda de bebidas**, com as seguintes características:

- Exibe um menu de bebidas com código, nome, valor e estoque.
- Permite ao cliente escolher a bebida e inserir o valor pago.
- Valida o valor inserido e calcula o troco (se houver), retornando as menores quantidades possíveis de notas e moedas.
- Atualiza o estoque automaticamente após a compra.
- Utiliza **funções e matrizes** para organização do código.

### Produtos disponíveis:

| ID | Produto    | Valor  | Estoque |
|----|------------|--------|---------|
| 1  | Coca-cola  | R$3,75 | 2       |
| 2  | Pepsi      | R$3,67 | 5       |
| 3  | Monster    | R$9,96 | 1       |
| 4  | Café       | R$1,25 | 100     |
| 5  | Redbull    | R$13,99| 2       |

---

## Como clonar e rodar o projeto

Mesmo que você nunca tenha usado o Git, siga este passo a passo:

### 1. Instale o Git

Se ainda não tem o Git instalado, baixe e instale por aqui:  
https://git-scm.com/

### 2. Clone o repositório para seu computador

Abra o terminal (Prompt de Comando ou Git Bash) e execute:

```bash
git clone https://github.com/Pedr0fsc/Maquina-de-vendas.git
```

Isso criará uma pasta com o nome `Maquina-de-vendas` contendo todos os arquivos do projeto.

### 3. Acesse a pasta do projeto

```bash
cd Maquina-de-vendas
```

### 4. Execute o projeto

Certifique-se de ter o **Python 3** instalado. Depois, no terminal, digite:

```bash
python maquina.py
```

---

## Como fazer alterações e enviar para o repositório

Se você fizer alguma modificação no código e quiser salvar no GitHub, siga este passo a passo:

### 1. Adicione as mudanças

```bash
git add .
```

### 2. Crie um commit com uma mensagem descritiva

```bash
git commit -m "Descrição da alteração feita"
```

Exemplo:
```bash
git commit -m "Adicionado cálculo de troco com moedas"
```

### 3. Envie as mudanças para o GitHub

```bash
git push
```

---

## Requisitos técnicos

- Python 3.x
- Terminal ou editor de código (recomendado: VSCode)
- Biblioteca padrão do Python (sem bibliotecas externas necessárias)

---

Se tiver dúvidas, fique à vontade para abrir uma [**issue**](https://github.com/Pedr0fsc/Maquina-de-vendas/issues) no repositório!

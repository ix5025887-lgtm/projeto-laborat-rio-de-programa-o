import json
import os

dados = {}
produtos = {}
financeiro = {}

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#dados.json

def carregar_dados(arquivo):
    global dados
    try:
        with open(arquivo, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
    except FileNotFoundError:
        dados = {"compras": [], "vendas": []}
        salvar_dados(arquivo)

def salvar_dados(arquivo):
    with open(arquivo, "w", encoding="utf-8") as arq:
        json.dump(dados, arq, indent=4, ensure_ascii=False)

#produtos.json

def carregar_produtos(arquivo):
    global produtos
    try:
        with open(arquivo, "r", encoding="utf-8") as arq:
            produtos = json.load(arq)
    except FileNotFoundError:
        produtos = {"produtos": []}
        salvar_produtos(arquivo)

def salvar_produtos(arquivo):
    with open(arquivo, "w", encoding="utf-8") as arq:
        json.dump(produtos, arq, indent=4, ensure_ascii=False)

def cadastrar_produto(nome, preco, custo, arquivo):
    novo_id = len(produtos["produtos"]) + 1
    produtos["produtos"].append({
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "custo": custo
    })
    salvar_produtos(arquivo)

def listar_produtos():
    print("\nPRODUTOS")
    for p in produtos["produtos"]:
        print(
            f'ID: {p["id"]} | {p["nome"]} | '
            f'Venda: R$ {p["preco"]:.2f} | '
            f'Custo: R$ {p["custo"]:.2f}'
        )

def consultar_lista(id_produto):
    for produto in produtos["produtos"]:
        if produto["id"] == id_produto:
            return produto
    return None

def editar_produto(id_produto, novo_nome, novo_preco, arquivo):
    for produto in produtos["produtos"]:
        if produto["id"] == id_produto:
            produto["nome"] = novo_nome
            produto["preco"] = novo_preco
            salvar_produtos(arquivo)
            print("Produto atualizado!")
            return
    print("Produto não encontrado!")

def deletar_produto(id_produto, arquivo):
    for produto in produtos["produtos"]:
        if produto["id"] == id_produto:
            produtos["produtos"].remove(produto)
            salvar_produtos(arquivo)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado!")

#financeiro.json

def carregar_financeiro(arquivo):
    global financeiro
    try:
        with open(arquivo, "r", encoding="utf-8") as arq:
            financeiro = json.load(arq)
    except FileNotFoundError:
        financeiro = {"faturamento": 0.0, "custos": 0.0, "lucro": 0.0}
        salvar_financeiro(arquivo)

def salvar_financeiro(arquivo):
    financeiro["lucro"] = financeiro["faturamento"] - financeiro["custos"]
    with open(arquivo, "w", encoding="utf-8") as arq:
        json.dump(financeiro, arq, indent=4, ensure_ascii=False)

def mostrar_financeiro():
    print("\nFINANCEIRO")
    print(f'Faturamento: R$ {financeiro["faturamento"]:.2f}')
    print(f'Custos: R$ {financeiro["custos"]:.2f}')
    print(f'Lucro: R$ {financeiro["lucro"]:.2f}')

def registrar_compra(descricao, valor, dados_arq, financeiro_arq):
    dados["compras"].append({
        "descricao": descricao,
        "valor": valor
    })
    financeiro["custos"] += valor
    salvar_dados(dados_arq)
    salvar_financeiro(financeiro_arq)

def registrar_venda(id_produto, quantidade, dados_arq, financeiro_arq):
    for produto in produtos["produtos"]:
        if produto["id"] == id_produto:
            faturamento = quantidade * produto["preco"]
            custo_total = quantidade * produto["custo"]

            dados["vendas"].append({
                "produto": produto["nome"],
                "quantidade": quantidade,
                "faturamento": faturamento,
                "custo": custo_total
            })

            financeiro["faturamento"] += faturamento
            financeiro["custos"] += custo_total
            salvar_dados(dados_arq)
            salvar_financeiro(financeiro_arq)
            return

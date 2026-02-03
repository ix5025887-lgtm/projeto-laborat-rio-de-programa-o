from funções import funções

def main():
    dados_arq = "dados.json"
    produtos_arq = "produtos.json"
    financeiro_arq = "financeiro.json"

    funções.carregar_dados(dados_arq)
    funções.carregar_produtos(produtos_arq)
    funções.carregar_financeiro(financeiro_arq)

    while True:
        funções.limpar_tela()
        print("SISTEMA DA CONFEITARIA")
        print("1 - Cadastrar produto")
        print("2 - Editar produto")
        print("3 - Listar produtos")
        print("4 - Registrar venda")
        print("5 - Registrar compra")
        print("6 - Ver financeiro")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço de venda: "))
            custo = float(input("Custo do produto: "))
            funções.cadastrar_produto(nome, preco, custo, produtos_arq)


        elif opcao == "2":
            funções.listar_produtos()
            idp = int(input("ID do produto: "))
            nome = input("Novo nome: ")
            preco = float(input("Novo preço: "))
            funções.editar_produto(idp, nome, preco, produtos_arq)

        elif opcao == "3":
            funções.listar_produtos()
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            funções.listar_produtos()
            idp = int(input("ID do produto: "))
            qtd = int(input("Quantidade: "))
            funções.registrar_venda(idp, qtd, dados_arq, financeiro_arq)

        elif opcao == "5":
            desc = input("Descrição da compra: ")
            valor = float(input("Valor: "))
            funções.registrar_compra(desc, valor, dados_arq, financeiro_arq)

        elif opcao == "6":
            funções.mostrar_financeiro()
            input("\nPressione ENTER para continuar...")

        elif opcao == "0":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida!")
            input("Pressione ENTER...")

if __name__ == "__main__":
    main()

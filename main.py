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
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Ler produto por ID")
        print("4 - Atualizar produto")
        print("5 - Deletar produto")
        print("6 - Registrar venda")
        print("7 - Registrar compra")
        print("8 - Ver financeiro")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            funções.listar_produtos()
            input("\nPressione ENTER para continuar...")

        elif opcao == "2":
            nome = input("Nome do produto: ")
            preco = float(input("Preço de venda: "))
            custo = float(input("Custo do produto: "))
            funções.cadastrar_produto(nome, preco, custo, produtos_arq)

        elif opcao == "3":
            try:
                idp = int(input("ID do produto: "))
                produto = funções.consultar_lista(idp)
                if produto:
                    print(produto)
                else:
                    print("Produto não encontrado!")
            except ValueError:
                print("ID inválido!")
            input("\nPressione ENTER para continuar...")

        elif opcao == "4":
            funções.listar_produtos()
            try:
                idp = int(input("ID do produto: "))
                nome = input("Novo nome: ")
                preco = float(input("Novo preço: "))
                funções.editar_produto(idp, nome, preco, produtos_arq)
            except ValueError:
                print("Dados inválidos!")
            input("\nPressione ENTER para continuar...")

        elif opcao == "5":
            funções.listar_produtos()
            try:
                idp = int(input("ID do produto a deletar: "))
                funções.deletar_produto(idp, produtos_arq)
            except ValueError:
                print("ID inválido!")
            input("\nPressione ENTER para continuar...")

        elif opcao == "6":
            funções.listar_produtos()
            idp = int(input("ID do produto: "))
            qtd = int(input("Quantidade: "))
            funções.registrar_venda(idp, qtd, dados_arq, financeiro_arq)

        elif opcao == "7":
            desc = input("Descrição da compra: ")
            valor = float(input("Valor: "))
            funções.registrar_compra(desc, valor, dados_arq, financeiro_arq)

        elif opcao == "8":
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

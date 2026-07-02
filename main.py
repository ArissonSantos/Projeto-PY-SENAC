estoque_produto = {
    1 : {"nome": "Teclado magnético", "preço": 650.00, "quantidade": 15},
    2 : {"nome" : "Teclado mecânico", "preço": 300.00, "quantidade": 15},
    3 : {"nome" : "Monitor FHD 27", "preço": 600.00, "quantidade": 5},
    4 : {"nome" : "Monitor QHD 27", "preço": 900.00, "quantidade": 5},
    5 : {"nome" : "Monitor QHD 32", "preço": 1200.00, "quantidade": 5},
    6 : {"nome" : "Mouse gamer Razer Purgatory 6400 dpi", "preço": 100.00, "quantidade": 25},
    7 : {"nome" : "Mouse gamer Redragon cobra 10000 dpi", "preço": 250.00, "quantidade": 15},
    8 : {"nome" : "Headset gamer Havit h4008", "preço": 300.00, "quantidade": 25}
}

selection = int
while selection != 0:

    print("[1] Visualizar estoque.")
    print("[2] Adicionar item ao carrinho.")
    print("[3] Visualizar carrinho.")
    print("[4] Finalizar compra.")
    print("[0] Sair.")
    selection = int(input("Escolha sua opção:"))

    if selection == 1:
        print(f"[visualizar estoque]")
        for key, content in estoque_produto.items():
            print(f"{content["nome"]} : quantidade: {content["quantidade"]}")

    elif selection == 2:
        print(f"[adicionar item ao carrinho]")
        id_produto = int(input("qual ID produto você deseja comprar?"))

        if id_produto in estoque_produto:
            prod_amnt = int(input("Quantas unidades você quer?"))
            if prod_amnt <= 0:
                print("Produto esgotado.")
                break
            elif prod_amnt < estoque_produto[id_produto]["quantidade"]:
                shop_cart.append(estoque_produto[id_produto])



    elif selection == 3:
        print(f"[visualizar carrinho]")
    elif selection == 4:
        print(f"[finalizar compra]")
    elif selection < 0:
        print("Opção inválida")
        break
    else:
        print("Saindo...")

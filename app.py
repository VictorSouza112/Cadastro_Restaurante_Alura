from opcoes import cad_rest, list_rest, atv_rest


# Função com as mensagens iniciais
def iniciar():
    print("""1
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
    """)


# Função para exibir o menu e fazer a escolha
def opcoes():
    restaurantes = {}

    while not (opcao_menu := input('\nMENU:\n1 - Cadastrar restaurante\n2 - Listar restaurante'
                                   '\n3 - Ativar restaurante\n4 - Sair\nDigite uma opção: ')) == '4':
        print('')  # Espaço para melhorar a formatação

        if opcao_menu == '1':
            restaurantes = cad_rest.cadastrar_restaurante(restaurantes)
        elif opcao_menu == '2':
            restaurantes = list_rest.listar(restaurantes)
        elif opcao_menu == '3':
            restaurantes = atv_rest.ativar(restaurantes)
        else:
            print('Opção inválida. Por favor, tente novamente.')

    print('Saindo do programa...')


iniciar()
opcoes()

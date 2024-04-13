from opcoes import cad_rest


# Função para ativar o restaurante
def ativar(restaurantes):
    cad_rest.print_line(char='-')
    print("ATIVAR RESTAURANTE")
    cad_rest.print_line(char='-')
    nome_restaurante = input('Digite o nome do restaurante: ')
    if nome_restaurante in restaurantes:
        restaurantes[nome_restaurante]['status'] = True  # Altere o status para True
        print(f"O restaurante {nome_restaurante} foi ativado com sucesso")
    else:
        print('Restaurante não encontrado.')
    cad_rest.print_line(char='-')
    return restaurantes

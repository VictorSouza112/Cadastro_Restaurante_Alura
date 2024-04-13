from opcoes import cad_rest


def listar_dados(nome_restaurante, tipo_comida):
    print(f'Nome: {nome_restaurante}\nComida: {tipo_comida}\n')


def listar(restaurantes):
    cad_rest.print_line(char='-')
    print("LISTA DE RESTAURANTES")
    cad_rest.print_line(char='-')
    for nome_restaurante, info in restaurantes.items():
        if info['status']:
            listar_dados(nome_restaurante, info['comida'])
    cad_rest.print_line(char='-')
    print('FIM DA LISTA')
    cad_rest.print_line(char='-')
    return restaurantes

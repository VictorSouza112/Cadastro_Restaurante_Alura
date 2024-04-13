def print_line(char='-'):
    print(char * 50)


def cadastrar_restaurante(restaurantes):
    print_line()
    print('CADASTRO DE RESTAURANTES')
    print_line()
    nome_restaurante = p_nome_restaurante()
    tipo_comida = p_tipo_comida()
    print('')
    restaurantes[nome_restaurante] = {'comida': tipo_comida, 'status': False}
    print_line()
    print(f'O restaurante {nome_restaurante} que serve {tipo_comida} foi cadastrado com sucesso')
    print_line()
    return restaurantes


def p_tipo_comida():
    return input('\nComida: ')  # Nova função para pegar o tipo de comida


def p_nome_restaurante():
    return input('\nNome: ')

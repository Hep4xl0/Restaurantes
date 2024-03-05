import os
restaurantes = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



def deletar_restaurante():
    clear_screen
    print('estas sao as opçoes de restarantes para serem deletados:')
    print(f'-{restaurantes}')
    restaurante_deletado = input('Qual sera deletado? ')
    try:
        restaurantes.remove(restaurante_deletado)
        print(f'o restaurante {restaurante_deletado} foi removido\n')
    except:
        print('falha em deletar restaurante\n')
    
    
    
def cadastrar_novo_restarante():
    clear_screen()
    print('cadastre um novo restaurante')
    nome_restaurante_novo = input('digite o nome do novo restaurante: ')
    categoria_restaurante_novo = input('digite a categoria do restaurante:')
    print(f'\nA categoria do restaurante é {categoria_restaurante_novo}.')
    dados_restaurante = {'nome':nome_restaurante_novo, 'categoria':categoria_restaurante_novo, 'status':False}
    restaurantes.append(dados_restaurante)
    print(f'resturante {nome_restaurante_novo} foi registrado com sucesso')
    
def mostrar_restaurantes():
    clear_screen()
        
    print('estes são os restaurantes:')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    input('clique enter para proseguir')
print('desejar iniciar atendimento?')
iniciar = str(input('sim/nao: ')).lower()

def editar_restaurantes():
    clear_screen()
    
    nome_restaurante = input('Digite o nome do restaurante que sera alterado')
    restauranta_encontrado = False 
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restauranta_encontrado =True
            restaurante['status'] =not restaurante['status']
            print(f'O restaurante {nome_restaurante} foi ativado com sucesso') if restaurante['status'] else print(f'O restaurante {nome_restaurante} foi desativado com sucesso')
    print ('retornando')





if iniciar == 'sim':
    while True:
        clear_screen()  
        print('''\n1.Criar novo restaurante:
    2.Listar restaurante
    3.Deletar restaurantes (nao funcional temp)
    4.Editar
              ''')
        
        opcao = int(input('escolha opcao: '))
        
        match opcao:
            case 1:
                cadastrar_novo_restarante()
            case 2:
                mostrar_restaurantes()
            case 3:
                deletar_restaurante()
            case 4:
                editar_restaurantes()
            case _:
                print('invalido')
            
else:
    print('atendimento encerrado')
    
    


    
    
   









    

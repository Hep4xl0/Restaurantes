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
    restaurantes.append(nome_restaurante_novo)
    print(f'\nrestaurante {nome_restaurante_novo} foi cadastrado com sucesso\n')

def mostrar_restaurantes():
    clear_screen()
        
    print('estes são os restaurantes:')
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    input('clique enter para proseguir')
print('desejar iniciar atendimento?')
iniciar = str(input('sim/nao: ')).lower()

if iniciar == 'sim':
    while True:
        clear_screen()  
        print('''\n1.Criar novo restaurante:
    2.Listar restaurante
    3.Deletar restaurantes
              ''')
        
        
        opcao = int(input('escolha opcao: '))
        
        match opcao:
            case 1:
                print('\nadicionar restaurante\n')
                cadastrar_novo_restarante()
            case 2:
                print('\nmostrar restaurante\n')
                mostrar_restaurantes()
            case 3:
                print('\nvamos remover um restaurante\n')
                deletar_restaurante()
            case _:
                print('invalido')
            
else:
    print('atendimento encerrado')
    
    


    
    
   









    

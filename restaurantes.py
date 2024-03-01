import os

restaurantes = []

def deletar_restaurante():
    print('estas sao as opçoes de restarantes para serem deletados:')
    print(restaurante)
    try:
        restaurante.remove(input('qual sera deletado? '))
        print(f'o restaurante {restaurante.remove} foi removido\n')
    except:
        print('falha em deletar restaurante\n')
    
    
    
def cadastrar_novo_restarante():
    os.system('cls')
    print('\ncadastre um novo restaurante')
    nome_restaurante_novo = input('digite o nome do novo restaurante: ')
    restaurantes.append(nome_restaurante_novo)
    print(f'\nrestaurante {nome_restaurante_novo} foi cadastrado com sucesso\n')



print('desejar iniciar atendimento?')
iniciar = str(input('sim/nao: ')).lower()

if iniciar == 'sim':
    while True:
        print('''\n\t1.Criar novo restaurante:
    2.Listar restaurante
    3.Deletar restaurantes
              ''')
        
        
        opcao = int(input('escolha opcao: '))
        
        match opcao:
            case 1:
                print('\nadicionar restaurante\n')
                cadastrar_novo_restarante()
            case 2:
                print('estes são os restaurantes:')
                for restaurante in restaurantes:
                    print(f'- {restaurante}')
            case 3:
                print('\nvamos remover um restaurante\n')
                deletar_restaurante()
            case _:
                print('invalido')
            
else:
    print('atendimento encerrado')
    
    


    
    
   









    

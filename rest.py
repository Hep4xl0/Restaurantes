
import os
restaurantes = []

class restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.status = False

    def apresentar(self):
        print(f'O restaurante: {self.nome} foi registrado, sua categoria é {self.categoria}, e seu status é {self.status}\n')

#######################################

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def inicio():
    clear_screen()
    print('desejar iniciar atendimento?')
    iniciar = input('sim/nao: ').lower()
    clear_screen()
    return iniciar

def mostrar_restaurantes():
    clear_screen()
        
    print('estes são os restaurantes:')
    for restaurante in restaurantes:
        print(f'- NOME: {restaurante.nome} | CATEGORIA: {restaurante.categoria} | STATUS: {restaurante.status}')
    input('clique enter para proseguir\n')

def adicionar_restaurante():
    clear_screen()
    print('Inicio do cadastramento\n')
    nome = input('digite nome: ')
    categoria = input('digite categoria: ')
    novo_restaurante = restaurante(nome, categoria)
    novo_restaurante.apresentar()
    restaurantes.append(novo_restaurante)
    input('clique enter para continuar:')

def deletar_restaurante():
    clear_screen()
    print('Estas sao as opcoes de restaurantes para serem deletados:')
    for restaurante in restaurantes:
        print(f'-Nome {restaurante.nome}')
    restaurante_deletado = input('Digite o nome do restaurante deletado: ')
    try:
        restaurante_removido = next(restaurante for restaurante in restaurantes if restaurante.nome == restaurante_deletado)
        restaurantes.remove(restaurante_removido)
        print(f'O restaurante {restaurante_deletado} foi removido\n')
    except:
        print('houve uma falha ao tentar deletar o restaurante\n')

    input('clique enter para continuar:')

def editar_restaurantes():
    clear_screen()
    print('Estas sao as opcoes de restaurantes para serem editados:')
    for restaurante in restaurantes:
        print(f'-Nome {restaurante.nome}')
    nome_restaurante = input('Digite o nome do restaurante que sera alterado: ')
    restauranta_encontrado = False 
    for restaurante in restaurantes:
        if nome_restaurante == restaurante.nome:
            restauranta_encontrado =True
            restaurante.status = not restaurante.status
            print(f'O restaurante {nome_restaurante} foi ativado com sucesso') if restaurante.status else print(f'O restaurante {nome_restaurante} foi desativado com sucesso\n')
        if not restauranta_encontrado:
            print('restaurante nao encontrado.\n')
        input('clique enter para continuar:')

#############################################


    
    


    
    
   









    

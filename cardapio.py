from rest import restaurante 
from rest import restaurantes

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')



cardapio = []

def __str__(self):
    return f"{self.nome} - Categoria: {self.categoria}, Preço: {self.preco}"


class item():
    def __init__(self, nome, categoria, preco, dono):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.dono = dono
        
    def __str__(self):
        return f"{self.nome} - {self.dono}"
        
class Filtro:
    def __init__(self, dono, restaurantes):
        self.dono = dono
        self.restaurantes = restaurantes
    
    def filtro(self, lista_itens):
        return [item for item in lista_itens if item.dono == self.dono and self.dono in [r.nome for r in self.restaurantes]]        


def menu():
    clear_screen()
    escolha = int(input('Bem vindo, oque deseja fazer?\n1.Registro de item\n2.Deletar Item\n3.Visualizar Itens\n4.Voltar\n> ' ))
    match escolha:
        case 1:
            registro_item()
        case 2:
            retirada_item()
        case 3:
            listagem_item()
        case 4:
            sair()
def registro_item():
    clear_screen()
    print('inicio registro do item')
    nome = input('Digite o nome do produto: ')
    categoria = input('Digite categoria: ')
    preco = float(input('Digite preço do item: '))
    input('\nVamos agora alocar este item em um restaurante!')
    print(f'Estes são os restaurantes possiveis para alocacao dos itens:')
    for restaurante in restaurantes:
        print(f'{restaurante.nome}')
    dono = input("Digite o nome de um dos restaurantes: ")
    try:
        verificação_existencia = next(restaurante for restaurante in restaurantes if restaurante.nome == dono)
        novo_item = item(nome, categoria, preco, dono)
        cardapio.append(novo_item)
        print('O item foi alocado com sucesso')
        print(f'O item {novo_item} foi registrado!')
        
    except:
        print('Cadastro invalido')
    
    
    input('clique enter para continuar:')    

def listagem_item():
    clear_screen()
    print('Estes são os restaurantes disponíveis para filtrar os itens:')
    for restaurante in restaurantes:
        print(restaurante.nome)
    restaurante_selecionado = input('Digite o nome do restaurante para filtrar os itens: ')
    itens_filtrados = Filtro(restaurante_selecionado, restaurantes).filtro(cardapio)
    print(f'Estes são os itens disponíveis no restaurante "{restaurante_selecionado}":')
    for item in itens_filtrados: 
        print(f'Nome: {item.nome} | Categoria {item.categoria} | Preço R${item.preco}')
    input('Pressione Enter para continuar: ')

def sair():
    escolha = str(input('Você tem certeza que deseja sair? Sim/Não '))
    if escolha == 'sim' or 'Sim':
        input('clique para voltar: ')
    elif escolha == 'Não' or 'Nao' or 'não' or 'nao':
        menu()



def retirada_item():
    clear_screen()
    print('Estes são os restaurantes disponíveis para filtrar os itens:')
    for restaurante in restaurantes:
        print(restaurante.nome)
    restaurante_selecionado = input('Digite o nome do restaurante para filtrar os itens: ')
    itens_filtrados = Filtro(restaurante_selecionado, restaurantes).filtro(cardapio)
    print(f'Estes são os itens disponíveis no restaurante "{restaurante_selecionado}":')
    for item in itens_filtrados: 
        print(f'Nome: {item.nome} | Categoria {item.categoria} | Preço R${item.preco}')
    restaurante_item_deletado =str(input('Digite nome do item a ser deletado: '))
    try:     
        restaurante_item_excluido = next(item for item in cardapio if item.nome == restaurante_item_deletado)
        cardapio.remove(restaurante_item_excluido)
        print(f"O item {restaurante_item_deletado} foi excluido")
    except:
        print('erro')

    input('clique enter para processeguir')
    
    
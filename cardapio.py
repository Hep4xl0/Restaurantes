from rest import restaurante 
from rest import restaurantes 
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


cardaio = []

class item():
    def __init__(self, nome, preco, categoria, dono):
        self.nome = nome
        self.preco = preco
        self.dono = dono
        self.categoria = categoria
    def __str__(self):
        return f"{self.nome} - {self.dono}
        
class filtro():
    def __init__(self, dono):
        self.dono = dono
    def filtro(self, lista_itens):
        return[item for item in lista_itens if item.dono == self.dono]
        


def menu():
    escolha = int(input('Bem vindo, oque deseja fazer?\n1.Registro de item\n2.Alocação de um item à um\n3.Deletar um item\n4.Listar os itens'))
    match escolha
        case 1:
            registro_item()
        case 2:
            alocacao_item()
        case 3:
            retirada_item()
        case 4:
            listagem_item()
    else
        print('atendimento encerrado.')
def registro_item():
    print('inicio registro do item')
    nome = input('Digite o nome do produto: ')
    categoria = input('Digite categoria: ')
    preco = int(input('Digite preço do item: '))            
    novo_item = item(nome, categoria, preco)
    print(f'O item {novo_item} foi registrado!')
    cardaio.append(novo_item)
    input('clique enter para continuar:')

def alocacao_item():
    for item in cardaio
    print(f'Estes são os restaurantes possiveis para alocacao dos itens: {item.nome}')

def retirada_item():


def listagem_item():

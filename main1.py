from rest import restaurante
from rest import restaurantes
from rest import adicionar_restaurante
from rest import deletar_restaurante
from rest import editar_restaurantes
from rest import mostrar_restaurantes
from cardapio import menu
from cardapio import item
from cardapio import registro_item
from cardapio import cardapio
from rest import inicio
from rest import clear_screen
import os

def main():
    pass
if __name__ == '__main__':
    main()

def program():
    iniciar = inicio()

    if iniciar == 'sim':
        while True: 
            clear_screen()
            print('''    1.Criar novo restaurante:
    2.Listar restaurante
    3.Deletar restaurantes
    4.Ativar/Desativar
    5.Cardapio
              ''')
        
            opcao = int(input('\tescolha opcao: '))
        
            match opcao:
                case 1:
                    adicionar_restaurante()
                case 2:
                    mostrar_restaurantes()
                case 3:
                    deletar_restaurante()
                case 4:
                    editar_restaurantes()
                case 5:
                    menu()
                case _:
                    print('invalido')
            
    else:
        print('atendimento encerrado')

main()
program()


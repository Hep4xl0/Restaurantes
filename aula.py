nome = input('Digite nomne: ')

nume_letra = len(nome)

print(f'o nome da pessoa é{nome} seu numero de letras é {nume_letra} a primeira letra do seu nome é {nome[0]}')

def soma(num1, num2):
    resultado = num1 + num2
    print(resultado)
def subtracao(num1, num2):
    resultado = num1 - num2
    print(resultado)
def divisao(num1, num2):
    resultado = num1 / num2
    print(resultado)
def multiplicacap(num1, num2):
    resultado = num1 * num2
    print(resultado)

num1 = int(input('digite num1 '))
num2 = int(input('digite num2 '))
tipo_de_operação = int(input('1.soma | 2.subtração | 3.divisão | 4.multiplicação: ' ))

match tipo_de_operação:
    case 1:
        soma(num1, num2)
    case 2:
        subtracao(num1, num2)
    case 3:
        divisao(num1, num2)
    case 4:
        multiplicacap(num1, num2)


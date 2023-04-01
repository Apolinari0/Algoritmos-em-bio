nome = input('Digite seu nome: ')
altura = float(input('digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura*altura)

print(f'{nome} tem {peso} kilos e altura de {altura} e portando o IMC é de {imc:.2f}.')

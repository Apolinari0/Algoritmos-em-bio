r01 = float(input("Digite valor da resistencia 01: "))
r02 = float(input("Digite valor da resistencia 02: "))
r03 = float(input("Digite valor da resistencia 03: "))

RR = 1/((1/r01)+(1/r02)+(1/r03)) #calculo da resistencia resultante;

print(f'Resistencia 1:{r01}, Resistencia 2:{r02}, Resistencia 3:{r03}. Valor da resistencia resultante: {RR:.2f}')


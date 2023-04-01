dias = int(input("dias: "))
horas = float(input('horas: '))
minutos = float(input('minutos: '))
segundos = float(input('segundos: '))

Tsegundos = dias*24*3600 + horas * 3600 + minutos * 60 + segundos

print(f'tempo em segundos: {Tsegundos}')
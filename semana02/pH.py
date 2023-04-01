pH = float(input("Digite o pH para consulta"))

if pH == 7:
  print(f'o pH em {pH} é Neutro.')
if pH > 7:
  print(f'o pH em {pH} é Acido')
if pH < 7:
  print(f'o pH em {pH} é Basico')

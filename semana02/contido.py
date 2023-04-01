str01 = str(input("String 1: "))
str02 = str(input("String 2: "))

for i in str01:
  if str01.find(str02):
    print(f'{str02} encontrado na posicao {str01.find(str02)} da string {str01}')
    break

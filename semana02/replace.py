str01 = str(input("String 01: "))
str02 = str(input('String 02: '))
str03 = str(input("String 03: "))
str04 = ""

str02.replace(str02,str03)

for i in str01:
  posicao = str02.find(i)
  if posicao != -1:
    str04 += str03[posicao]
  else:
    str04 += i
  
  
  
print(f'{str04}')


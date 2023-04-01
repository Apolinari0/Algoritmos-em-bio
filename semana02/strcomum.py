str01 = str(input("String 1: "))
str02 = str(input("String 2: "))
str03 = ""

#verifica se str01 é maior que a str02 para percorrer a string

if len(str01) > len(str02):
  for i in str01:
    if i in str02:
      str03 += i
#se str01 nao é maior, percorre a segunda,
else:
  for i in str02:
    if i in str01:
      str03 += i

print(str03)
salario = float(input("Digite seu salário: "))
aumento = float(input("Digite o aumento salarial: "))

NewSalario = salario + (salario * aumento/100)

print(f'Seu salário anterior:{salario}. Salário novo:{NewSalario}')
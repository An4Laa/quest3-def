# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento

def salario():
    salario = float(input("Insira seu salário: "))
    porcentagem = (salario * 15.0) / 100.0
    print("Seu novo sálario será de...")
    print(salario + porcentagem)

salario()
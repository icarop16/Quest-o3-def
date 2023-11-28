#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
def aumento (salario):
    aumento = salario + (salario * 15)/100 
    print (f"Seu novo salário é de {aumento}")
salario = float(input(f"Adicione o valor do seu salário: "))
aumento(salario)
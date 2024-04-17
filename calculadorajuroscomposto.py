nome = input("Qual seu Nome?: ")
print('|------------------------------------------- :) -----------------------------------------|')
print(" ")
print(f"Olá {nome}, seja bem vindo a : Calculadora de Juros Compostos!")
print(" ")
print('|------------------------------------------- :) -----------------------------------------|')
print(" ")
dinheiro_inicial = int(input("Digite a quantidade inicial do investimento: "))
tempo = int(input("Digite quantos anos você deixara o dinheiro sendo investido: "))
taxa = float(input("Digite, em decimal, qual a taxa anual de retorno do seu investimento: "))
salario_desejado = int(input("Digite o salario mensal que deseja receber ao aposentar: "))

montante = dinheiro_inicial * (1 + taxa) ** tempo
montante = round(montante, 2)
print(" ")
print('|------------------------------------------- :) -----------------------------------------|')
print(" ")
print(f"Parabéns {nome}, ao final do periodo de {tempo} anos com o investimento de R${dinheiro_inicial} você terá R${montante} !  ")
salario_mensal = (montante * taxa)/12
salario_mensal = round(salario_mensal, 2 )

if salario_mensal >= salario_desejado:
    print(f"Parabéns, você pode se aposentar seu salario mensal com esse montante é R$ {salario_mensal} ;) ")

elif salario_mensal < salario_desejado:
    print(f"Infelizmente se aposentar não se torna viavel com esse montante :( ")

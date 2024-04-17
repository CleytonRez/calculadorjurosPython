nome = input("Qual seu Nome?: ")
print('|------------------------------------------- :) -----------------------------------------|')
print(" ")
print(f"Olá {nome}, seja bem vindo a : Calculadora de Juros Compostos!")
print(" ")
print('|------------------------------------------- :) -----------------------------------------|')
print(" ")
dinheiro_inicial = int(input("Digite a quantidade inicial do investimento: "))
tempo_desejado = int(input("Digite quantos meses você deixara o dinheiro sendo investido: "))
taxa = float(input("Digite, em decimal, qual a taxa mensal de retorno do seu investimento: "))
aporte = int(input("Digite quanto dinheiro você consegue aportar por mês: "))
salario_desejado = int(input("Digite o salario mensal que deseja receber ao aposentar: "))
montante = 0

tempo_decorrido = 0

while tempo_decorrido < tempo_desejado:
    if tempo_desejado == 0:
        montante = dinheiro_inicial * (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido = tempo_decorrido + 1

    else:
        montante = (montante + aporte) * (1 + taxa) ** 1
        montante = round(montante, 2)
        tempo_decorrido = tempo_decorrido + 1


print(" ")
print('|------------------------------------------- :) -----------------------------------------|')
print(" ")
print(f"Parabéns {nome}, ao final do periodo de {tempo_desejado} anos com o investimento de R${dinheiro_inicial} você terá R${montante} !  ")
salario_mensal = (montante * taxa)
salario_mensal = round(salario_mensal, 2 )

if salario_mensal >= salario_desejado:
    print(f"Parabéns, você pode se aposentar seu salario mensal com esse montante é R$ {salario_mensal} ;) ")

elif salario_mensal < salario_desejado:
    print(f"Infelizmente se aposentar não se torna viavel com esse montante :( ")

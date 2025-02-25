'''
Programa: Soma
Descrição: Armazena os números 2 e 3 e imprime a soma na tela 
Autor: Arthur Gaspareto
Data: 25/02/25
Versão: 0.0.2
Novidades da Versão

25/02/2025
Nesta versão:
1.Armazena os números 2 e 3 e imprime a soma na tela
2.O usuário digita os números a serem somados
'''

#Alocação de Memória
soma = float()
num1 = float()
num2 = float()

#Entrada de Dados

num1 = float(input('Qual o primeiro número?'))
num2 = float(input('Qual o segundo número?'))

#Processamento de Dados
soma = num1 + num2


#Saída de dados

print(f'A soma dos números digitados é: {soma}')
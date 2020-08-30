#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

pergunta = input('Deseja continuar? S/N     ')
pergunta.upper()
valor = int(input('Digite um numero: '))
lista = []

while pergunta == 'S':
  lista.append(valor)
  pergunta = input('Deseja continuar? S/N    ')
  pergunta.upper()
  valor = int(input('Digite um numero: '))

print('--------------------------------------------------------')
print('Você digitou', len(lista), 'elementos')
print(sorted(lista, reverse = True))
if 5 in lista:
  print('O numero 5 está na lista')
else:
  print('O numero 5 não está na lista')
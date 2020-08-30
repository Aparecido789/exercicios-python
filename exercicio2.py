#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
while True:
  lista.append(int(input('Digite um numero: ')))
  pergunta = input('Deseja continuar? {S/N}  ')
  if pergunta in 'Nn':
    break

print('-' * 30)
print('Você digitou', len(lista), 'elementos')
print(sorted(lista, reverse = True))
if 5 in lista:
  print('O numero 5 está na lista')
else:
  print('O numero 5 não está na lista')
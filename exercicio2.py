#Crie um programa que vai ler v�rios n�meros e colocar em uma lista. Depois disso, mostre:
# A) Quantos n�meros foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e est� ou n�o na lista.

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
print('Voc� digitou', len(lista), 'elementos')
print(sorted(lista, reverse = True))
if 5 in lista:
  print('O numero 5 est� na lista')
else:
  print('O numero 5 n�o est� na lista')
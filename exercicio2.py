#Crie um programa que vai ler v�rios n�meros e colocar em uma lista. Depois disso, mostre:
# A) Quantos n�meros foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e est� ou n�o na lista.

lista = []
while True:
  lista.append(int(input('Digite um numero: ')))
  pergunta = input('Deseja continuar? {S/N}  ')
  if pergunta in 'Nn':
    break

print('-' * 30)
print('Voc� digitou', len(lista), 'elementos')
print(sorted(lista, reverse = True))
if 5 in lista:
  print('O numero 5 est� na lista')
else:
  print('O numero 5 n�o est� na lista')
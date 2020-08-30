#Elabore	um	programa	em	Python	que	calcule	o	resultado	de	nx, onde	n	e	x	são	 números	inteiros	 positivos	lidos.	 Por	exemplo,	 se	 n	 =	 2	e	x	 =	 3,	 o	 valor	 2^3 =	 8.	 Para	 o	 cálculo,	 use	 apenas	 os	 comandos	 iterativos	 do	 Python	 e	 as	 operações aritméticas	de	soma,	subtração,	multiplicação	e	divisão	(não	use	as	funções	prédefinidas	de	Pyhton).	Lembre-se,	quando	x	=	0,	o	resultado	é	1,	independente	do	valor	de	n.

n = int(input('Digite a base: '))
x = int(input('Digite o expoente: '))
soma = 1
contador = 1
if x == 0:
    soma = 1
    print('O resultado é: ', soma)
else:
    while (contador <= x):
        soma *= n
        contador += 1
    print('O resultado é: ', soma)

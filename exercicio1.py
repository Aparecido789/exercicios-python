#Elabore	um	programa	em	Python	que	calcule	o	resultado	de	nx, onde	n	e	x	s�o	 n�meros	inteiros	 positivos	lidos.	 Por	exemplo,	 se	 n	 =	 2	e	x	 =	 3,	 o	 valor	 2^3 =	 8.	 Para	 o	 c�lculo,	 use	 apenas	 os	 comandos	 iterativos	 do	 Python	 e	 as	 opera��es aritm�ticas	de	soma,	subtra��o,	multiplica��o	e	divis�o	(n�o	use	as	fun��es	pr�definidas	de	Pyhton).	Lembre-se,	quando	x	=	0,	o	resultado	�	1,	independente	do	valor	de	n.

n = int(input('Digite a base: '))
x = int(input('Digite o expoente: '))
soma = 1
contador = 1
if x == 0:
    soma = 1
    print('O resultado �: ', soma)
else:
    while (contador <= x):
        soma *= n
        contador += 1
    print('O resultado �: ', soma)

# Altere o exercício anterior para que o
#usuário informa a quantidade de valores
# que deseja inserir, insira esses
#valores e mostre a quantidade de valores
#pares e ímpares existentes na lista.
valores = []
soma = 0
i = 0
valor = int(input('Quantos números deseja inserir : '))
while i < valor:
    numeros = int(input('Digite os  números: '))
    valores.append(numeros)
    i+=1
pares=0
impares=0
for valor in valores:
    if (numeros % 2) == 0:
        pares += 1
    else:
        impares += 1
print('\nPares{pares} :' ,pares)
print('\nImpares{inpares} :',impares)
print('Lista :',valores)
''' 14/03/2020 by jan Mesu
Crie um programa que peça um número
e mostre seu dobro, seu triplo e sua raíz quadrada
'''

numero       = int(input('Escreva um número: '))
dobro        = numero * 2
triplo       = numero * 3

print(
f""" O número digitado foi {numero}

O dobro de {numero} é {dobro}

O triplo de {numero} é {triplo}

A raíz quadrade de {numero} é {float(numero)**0.5:.2f}
""" )
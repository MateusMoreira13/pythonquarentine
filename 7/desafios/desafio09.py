''' 13/03/2020 by jan Mesu
Faça um programa que peça um número inteiro qualquer
e mostre a sua tabuada.
'''

numero = int(input('Escreva um número para ver a tabuada dele: '))

print(
f"""
1  x{numero:>5}
2  x{numero*2:>5}
3  x{numero*3:>5}
4  x{numero*4:>5}
5  x{numero*5:>5}
4  x{numero*6:>5}
7  x{numero*7:>5}
8  x{numero*8:>5}
9  x{numero*9:>5}
10 x{numero*10:>6}
""")
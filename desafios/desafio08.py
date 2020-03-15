''' 13/03/2020 by jan Mesu
Escreba un programa que haga un conversor de metros para centímetros y milímetros
después imprima el resultado
'''

metros      = float(input('Escreva um valor em metros '))
centimetros = metros * 100
milimetros  = metros * 1000
kilometros  = metros / 1000
decametros  = metros / 10
hectametro  = metros / 100
print(f"""{metros} Metros tem:\n{centimetros} centímetros\n{milimetros} milímetros
Quilometros {kilometros}\nDecâmetros {decametros}\nHectametros {hectametro}
""")

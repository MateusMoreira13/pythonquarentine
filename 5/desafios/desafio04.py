''' 13/03/2020 by jan Mesu
Escreva um valor e printe o tipo primitivo
e todas as informações sobre ele.
'''
n = input('Digite alguma coisa: ')

print(
f"""
O tipo primitivo de {n} é {type(n)}
Alphanumerico {n.isalpha()}

É numerico {n.isnumeric()}

lowercase {n.islower()}

Idenficador {n.isidentifier()}

Digito {n.isdigit()}

Title {n.istitle()}

Printavel {n.isprintable()}

uppercase {n.isupper()}

Space {n.isspace()}
""")
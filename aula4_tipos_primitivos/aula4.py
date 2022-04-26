"""
Tipos de dados

str - string - tetos 'Assim', "Assim"
int - inteiro - 123456, 0, -10, -20, -1500
float - real/ponto flutuante - 10.50, 1.5, -10.10
bool- booleano/lógico - True, False, 10==10 -> True
"""
print('Luiz', type('Luiz'))
print('10', type('10'))
print('10.50', type('10.50'))
print('False', type('False'))
print('20==20', type('20==20'))
print('l==L', type('l==L'))
print(10, type(10))
print(25.23, type(25.23))
print(10==10, type(10==10))
print('l'=='L', type('l'=='L'))

print('Luiz', type('Luiz'), bool('Luiz'))  
# bool('Luiz') == True porque quando há conteúdo, é gerado o valor True,
# quando não há, False.

print('10', type('10'), type(int('10')))
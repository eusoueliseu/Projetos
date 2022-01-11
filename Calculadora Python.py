#!/usr/bin/env python
# coding: utf-8

# In[48]:

print('''#### Calculadora Python ####

Digite a operação desejada

1 - SOMA
2 - SUBTRAÇÃO
3 - MULTIPLICAÇÃO
4 - DIVISÃO
''')

valores = (1, 2, 3, 4)
conta = 0

operacao = int(input('Operação desejada: '))

if operacao > 4:
    conta = 'Operação inexistente'
elif operacao == 1:
    conta = 'Operação SOMA selecionada'
elif operacao == 2:
    conta = 'Operacação SUBTRAÇÃO selecionada'
elif operacao == 3:
    conta = 'Operação MULTIPLICAÇÃO selecionada'
elif operacao == 4:
    conta = 'Operação DIVISÃO selecionada'

    
    
print (conta)
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2

try:
    divisao = valor1 / valor2
except ZeroDivisionError:
    print('Impossível dividir por 0')

if operacao == 1:
    resultado = soma
elif operacao == 2:
    resultado = subtracao
elif operacao == 3:
    resultado = multiplicacao
else:
    resultado = divisao

resultado = str(resultado)
    
a = ['Resultado: ', resultado]
b = str('')

if (operacao == 4) and (valor2 == 0):
    print (b)
else:
    print (a)

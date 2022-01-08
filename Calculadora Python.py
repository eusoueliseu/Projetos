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

if operacao in valores:
    if operacao == 1:
        conta = 'Operação SOMA selecionada'
    elif operacao == 2:
        conta = 'Operacação SUBTRAÇÃO selecionada'
    elif operacao == 3:
        conta = 'Operação MULTIPLICAÇÃO selecionada'
    elif operacao == 4:
        conta = 'Operação DIVISÃO selecionada'
else:
    print ('Operação inválida')
    
print (conta)
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))

soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1 / valor2

if operacao == 1:
    resultado = soma
elif operacao == 2:
    resultado = subtracao
elif operacao == 3:
    resultado = multiplicacao
else:
    resultado = divisao

print ('Resultado: ', resultado)


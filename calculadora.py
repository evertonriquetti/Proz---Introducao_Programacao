# -*- coding: utf-8 -*-
"""calculadora.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R87SPZncTsR98Y0SgymstKblW9huGsSn
"""

# Definindo a função calculadora
def calculadora(num1, num2, operacao):
  # Verificando qual operação foi escolhida
  if operacao == 1: # Soma
    return num1 + num2
  elif operacao == 2: # Subtração
    return num1 - num2
  elif operacao == 3: # Multiplicação
    return num1 * num2
  elif operacao == 4: # Divisão
    return num1 / num2
  else: # Operação inválida
    return 0

# Testando a função com alguns exemplos
print(calculadora(5, 3, 1)) # Deve imprimir 8
print(calculadora(5, 3, 2)) # Deve imprimir 2
print(calculadora(5, 3, 3)) # Deve imprimir 15
print(calculadora(5, 3, 4)) # Deve imprimir 1.6666666666666667
print(calculadora(5, 3, 5)) # Deve imprimir 0
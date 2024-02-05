# -*- coding: utf-8 -*-
"""Calculadora2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XZ4xiBh_gSCH6T-jNExH2Jqn-wzwYTdF
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
    return None

# Iniciando o programa
while True: # Repete o programa até que o usuário saia
  # Mostrando as opções de operação
  print("Escolha uma das opções abaixo:")
  print("1: Soma")
  print("2: Subtração")
  print("3: Multiplicação")
  print("4: Divisão")
  print("0: Sair")

  # Pedindo ao usuário que digite a opção desejada
  opcao = int(input("Digite o número da operação: "))

  # Verificando se o usuário quer sair
  if opcao == 0:
    print("Obrigado por usar a calculadora. Até mais!")
    break # Sai do laço while

  # Pedindo ao usuário que digite os dois números da operação
  n1 = float(input("Digite o primeiro número: "))
  n2 = float(input("Digite o segundo número: "))

  # Chamando a função calculadora com os números e a opção escolhida
  resultado = calculadora(n1, n2, opcao)

  # Verificando se o resultado é válido
  if resultado is not None:
    # Mostrando o resultado na tela
    print(f"O resultado da operação é: {resultado}")
  else:
    # Mostrando uma mensagem de erro
    print("Essa opção não existe. Tente novamente.")
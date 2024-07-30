''' 
criando um algoritmo que mostra o imc para o usuário.
'''

def imc(peso, altura):
    imc = round(peso / (altura**2), 2)
    return imc

def result_imc():
    if imc(peso, altura) < 18.5:
        print(f'Seu imc é {imc(peso, altura)} Você está abaixo do peso.')
    elif imc(peso, altura) < 24.9 and imc(peso, altura) >= 18.5:
        print(f'Seu imc é {imc(peso, altura)} Você está com o peso adequado.')
    elif imc(peso, altura) < 29.9 and imc(peso, altura) >= 25:
        print(f'Seu imc é {imc(peso, altura)} Você está com sobrepeso.')
    elif imc(peso, altura) < 34.9 and imc(peso, altura) >= 30:
        print(f'Seu imc é {imc(peso, altura)} Você está com obesidade de primeiro grau.')
    elif imc(peso, altura) < 39.9 and imc(peso, altura) >= 35:
        print(f'Seu imc é {imc(peso, altura)} Você está com obesidade de segundo grau.')
    else:
        print(f'Seu imc é {imc(peso, altura)} Você está com obesidade extrema.')
    return result_imc

peso = float(input('Qual seu peso em kg? '))
altura = float(input('Qual sua altura em m? '))

imc(peso, altura)
result_imc()

'''
IMC <18,5kg/m2 - baixo peso.
IMC >18,5 até 24,9kg/m2 - eutrofia (peso adequado)
IMC ≥25 até 29,9kg/m2 - sobrepeso.
IMC >30,0kg/m2 até 34,9kg/m2 - obesidade grau 1.
IMC >35kg/m2 até 39,9kg/m2 - obesidade grau 2.
IMC > 40kg/m2 - obesidade extrema.
'''
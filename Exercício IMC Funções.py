# calculo IMC peso / (altura*altura) função:
def imc(peso, altura):
    imc = peso / (altura*altura)
    return imc

def class_imc (sexo, peso, altura):
    valor_imc = imc(peso, altura)
    if sexo == 'm':
        if valor_imc < 20.7:
            return 'Abaixo do peso.'
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return 'peso normal.'
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return 'Marginalmente acima do peso.'
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return 'peso acima do ideal.'
        elif valor_imc >= 31.1:
            return 'Obesidade'
        else: 'Erro de cálculo'

    if sexo == 'f':
        if valor_imc < 19.1:
            return 'Abaixo do peso.'
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return 'peso normal.'
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return 'Marginalmente acima do peso.'
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return 'peso acima do ideal.'
        elif valor_imc >= 31.1:
            return 'Obesidade'
        else:
            'Erro de cálculo'

# Inputs e validação de dados das variaveis.
valid = False
while not valid:
    sexo = input("Digite seu sexo 'M', para masculino ou 'F', para feminino: ").lower()
    if sexo != "m" and sexo != "f":
        print("Por favor use apenas 'M' para masculino ou 'F' para feminino.")
    else:
        valid = True

valid = False
while not valid:
    peso = input('digite seu peso:')
    try:
        peso = float(peso)
        if peso <= 0:
            print("O peso inserido deve ser maior que 0.")
        else:
            valid = True
    except:
        print('Formato incorreto utilize apenas numeros e pontos exemplo: 75.50')
valid = False
while not valid:
    altura = input('Digite sua altura:')
    try:
        altura = float(altura)
        if altura <= 0:
            print("A altura inserida deve ser maior que 0.")
        else:
            valid = True
    except:
        print('Formato incorreto utilize apenas numeros e pontos exemplo: 1.70')
v_imc = imc(peso, altura)
c_imc = class_imc(sexo, peso, altura)

print('O seu IMC é:', v_imc)
print('A sua classificação é:', c_imc)



valid = False
while valid == False:
    peso1 = input("Digite qual o peso da primeira prova:")
    try:
        peso1 = float(peso1)

        if peso1 <= 0:
            print('O valor da do peso da prova deve ser maior que 0')
        else:
            valid = True

    except:
        print("Formato incorreto utilize apenas numeros e pontos exemplo: 7.5")
valid = False
while valid == False:
    peso2 = (input("Digite qual o peso da segunda prova:"))
    try:
        peso2 = float(peso2)
        if peso2 <= 0:
            print('O valor da do peso da prova deve ser maior que 0')
        else:
            valid = True
    except:
        print("Formato de preço incorreto utilize apenas numeros e pontos exemplo: 7.5")

valid = False

while valid == False:
    nota1 = (input("Digite a nota da primeira prova:"))
    try:
        nota1 = float(nota1)
        if nota1 < 0:
            print('O valor da nota não pode ser negativo.')
        else:
            valid = True
    except:
        print("Formato de preço incorreto utilize apenas numeros e pontos exemplo: 7.5")
valid = False

while valid == False:
    nota2 = (input("Digite a nota da segunda prova:"))
    try:
        nota2 = float(nota2)
        if nota2 < 0:
            print('O valor da nota não pode ser negativo.')
        else:
            valid = True
    except:
        print("Formato de preço incorreto utilize apenas numeros e pontos exemplo: 7.5")


media1 = (nota1*peso1)+(nota2*peso2)
media2 = peso1+peso2
media = media1 / media2

print('A média desse aluno é: ',media)
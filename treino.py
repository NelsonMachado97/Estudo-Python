peso1 = int(input("Digite qual o peso da prova:"))
peso2 = int(input("Digite qual o peso da segunda prova:"))

nota1 = int(input("Digite a nota da primeira prova:"))
nota2 = int(input("Digite a nota da segunda prova:"))

media1 = (nota1*peso1)+(nota2*peso2)
media2 = peso1+peso2
media = media1 / media2

print('A média desse aluno é: ',media)
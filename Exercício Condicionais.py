nome_aluno = input('Digite o nome do aluno a seguir: ').lower()

nota_1 = float(input('Digite a 1ª nota: '))
nota_2 = float(input('Digite a 2ª nota: '))

peso1 = float(input("Digite qual o peso da prova:"))
peso2 = float(input("Digite qual o peso da segunda prova:"))

total_faltas = int(input('Informe o numero de faltas do aluno: '))
total_aulas = 20
total_presença = total_aulas - total_faltas
presença = int((total_presença / total_aulas)*100)

media1 = (nota_1*peso1)+(nota_2*peso2)
media2 = peso1+peso2
media = media1 / media2

if presença >= 70 and media >= 6.0:
    print(nome_aluno, 'aprovado!! média:',media ,'e a presença foi de' ,presença, '%')

elif presença < 70 and media < 6.0:
    print(nome_aluno, 'reprovado por média e por faltas.')

elif presença < 70:
    print(nome_aluno, 'reprovado por faltas, acima de 70% o aluno só compareceu:',presença, '%')

elif media < 6.0:
    print(nome_aluno, 'reprovado por média inferior a 6.0 media:', media)

else:
    print('Erro na entrada de dados, tente novamente.')





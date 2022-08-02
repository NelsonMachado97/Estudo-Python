valores = {}
x = 's'
valid_preço = False
while x == 's':
    produto = input('Qual produto que está sendo vendido?: ').lower()

    while valid_preço == False:
        valor = (input('Digite o valor do produto: '))
        try:
            valor = float(valor)

            if valor <= 0:
                print('O preço tem que ser maior que 0')
            else:
                valid_preço = True

        except:
            print("Formato de preço incorreto utilize apenas numeros e pontos exemplo: 10.50")
    valid_preço = False

    x = input('Deseja adicionar outro produto? (S ou N): ').lower()
    valores[produto] = valor

total = 0
for i in valores:
    total += valores[i]
    print(i,':', valores[i])

print('Soma dos produtos:',total)
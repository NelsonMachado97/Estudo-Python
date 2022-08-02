cores = {'vermelho': 'Red', 'azul': 'blue', 'rosa': 'pink', 'roxo': 'purple'}

cor = input("Qual cor quer traduzir para o inglês? ").lower()
print('A cor '+ cor + ' em inglês traduz para: '+ cores.get(cor, 'Desculpe, esta cor não consta no meu dicionário.'))
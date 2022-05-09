#Renda Per Capita Familiar
print('Vamos calcular a renda per capita de sua família.')

contador = 0
pessoas = int(input('Quantas pessoas moram com você?'))
proletario = int(input('Quantas pessoas possuem renda fixa?'))
salario = 0 
renda = 0 
soma = 0

while contador < proletario:
    contador = contador + 1
    salario  = int(input(f'Digite o {contador}° salário.'))
    soma = soma + salario
    renda = soma / pessoas
print(f'Sua renda per capita familiar é de {renda}')

if renda < 1100 or renda == 1100:
    print('\nSua renda é menor ou igual a um salário minímo por pessoa. \nPortanto, você tem direito a concorrer a bolsas estudantis e isenção de taxas de vestibulares.')
else:
    print('\nSua renda é maior que um salário minímo por pessoa. \nPortanto,você não tem direito à isenção de vestibulares.')
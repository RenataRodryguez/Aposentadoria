# Confira sua aposentadoria 
nome = input("Oi, qual seu nome?").title()
print("Olá,", nome)

generos = ["feminino", "masculino"]

print("Escolha seu gênero:")
print("1 - Feminino")
print("2 - Masculino")

escolha = int(input(f'{nome}, digite o número correspondente ao seu gênero:'))

if escolha == 1:
    genero_selecionado = generos[0]
elif escolha == 2:
    genero_selecionado = generos[1]
else:
    print("Opção inválida")

idade = int(input("Digite sua idade"))
#idade                    
if idade < 55:
    print(f'Desculpe {nome} você ainda não pode se aposentar')
    quit()

trabalho = ["Rural", "Não rural"]

print(f'{nome}, escolha seu tipo de trabalho:')
print("1 - Rural")
print("2 - Não Rural")

escolha_trabalho = int(input("Qual seu tipo de trabalho?"))
print(f'Sua escolha de trabalho é {escolha_trabalho}')

if escolha_trabalho == 1:
    trabalho_selecionado = trabalho[0]
elif escolha_trabalho == 2:
    trabalho_selecionado = trabalho[1]    

#homens
if genero_selecionado == "masculino" and idade >= 60 and trabalho_selecionado == "Rural":
    print("Parabéns, você pode se aposentar") 
elif genero_selecionado == "masculino" and idade >= 65 and trabalho_selecionado == "Não rural":
    print("Parabéns você pode se aposentar")
#mulheres
elif genero_selecionado == "feminino" and idade >= 55 and trabalho_selecionado == "Rural":
    print("Parabéns você pode se aposentar")
elif genero_selecionado == "feminino" and idade >= 62 and trabalho_selecionado == "Não rural":
    print("Parabéns você pode se aposentar")
else:
    print(f"Desculpe {nome}, Você não pode se aposentar!")
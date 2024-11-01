# solicitando ao usuario sua altura
altura = float(input("Digite a sua altura por favor: "))

# solicitando ao usuario seu peso
peso = float(input("Digite o seu peso por favor: "))

#fazendo o calculo do imc
imc = peso / (altura * altura)

#Utilizando if e elif para saber em qual grupo que essa pessoa está
#A lógica seria se o 'imc' for menos que 18.5 ele fica abaixo do peso, senão se ele fica em alguma cadegoria, senão ele é obesidade grau 3
if imc < 18.5:
    #todas tem um print para saber em qual grupo ele caiu
    print("Abaixo do Peso")
elif imc >= 18.5 and imc < 24.9:
    print("Peso Normal")
elif imc >= 24.9 and imc < 29.9:
    print("Sobrepeso")
elif imc >= 29.9 and imc < 34.9:
    print("Obesidade Grau 1")
elif imc >= 34.9 and imc < 39.9:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3 (Mórbida)")

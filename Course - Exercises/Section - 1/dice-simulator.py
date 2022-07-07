import random
import statistics

def gerar_numeros(faces):
    dados = input("Digite o número de dados: ")
    dados = int(dados)
    numeros = []
    for i in range(dados):
        numero = random.randint(1, faces)
        numeros.append(numero)
        print("Seu número é: %s" % numero)
    print('A soma é: %s' % sum(numeros))
    print('O valor máximo é: %s' % max(numeros))
    print('O valor mínimo é: %s' % min(numeros))
    print('A média é: %s' % statistics.mean(numeros))

continua = True
while continua:
    faces = input("Digite um número de faces (ou 'parar' para acabar o programa): ")
    if faces == "parar":
        continua = False
    else:
        faces = int(faces)
        gerar_numeros(faces)
print("Finalizou o programa")
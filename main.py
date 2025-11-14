import random

min = 1
max= 100
numeroCerto = random.randint(min, max)
maximo = 10

print("Bem-vindo ao jogo de adivinhação para provaaaa")
print(f"O número secreto está entre {min} e {max}.")


for tentativa in range(1, maximo + 1):
   
    numeroColocado = int(input(f"Tentativa {tentativa} de {maximo}. Faça seu palpite: "))
    if numeroColocado == numeroCerto:
        print(f"Parabéns! Você acertou o número secreto {numeroCerto} em {tentativa} tentativas.")
        break
    elif numeroColocado < numeroCerto:
        print("é maior")
    else:
        print("é menor")
else:
    print(f"Você chegou no numero maximo de tentativas. O número era {numeroCerto}.")
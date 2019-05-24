import random

print("******************", "JOGO DA ADVINHACAO", "******************", sep="\n")

numero_secreto = random.randint(0, 100)

while True :
    chute = int(input("Qual o seu chute? "))
    if numero_secreto == chute :
        print("Na mosca!", end="\n\n")
        break
    elif chute < numero_secreto :
        print("Tente um numero maior", end="\n\n")
    elif chute > numero_secreto :
        print("Tente um numero menor", end="\n\n")
    

numero_secreto = 7
tentativas_maximas = 3
tentativas = 0

print("Tente adivinhar o número entre 1 e 10.")

while tentativas < tentativas_maximas:
    palpite = int(input("Digite um número: "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    else:
        print("Errado! Tente novamente.")
else:
    print("Que pena! Você esgotou suas tentativas.")

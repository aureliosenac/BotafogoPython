conta = 1
soma = 0
lista=[]
while conta != 0:
    num1 = int(input("digite número inteiro - para encerrar digite 0 "))
    if num1 != 0:
        # lista.append(num1)
        conta += 1 
        soma = soma + num1
    else:    
        conta = conta - 1
        media = soma / conta
        print("quantidade de números ",conta)
        print("media aritmética ",media)
        conta = 0
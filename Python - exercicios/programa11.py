# programa recebe dois numeros inteiros
# e imprime intervalo entre eles.

num1 =int(input("digite um numero inteiro "))
num2 =int(input("digite outro numero inteiro "))
intervalo =int(num2 - num1)
n1 = num1 + 1
n2 = num2 - 1
soma = 0
condicao = True
while condicao:
   print(n1, end=' ')
   soma = soma + n1
   n1 = n1 + 1
   if n1 == num2:
      condicao = False
      
print("soma: ", soma)      
      
    
    

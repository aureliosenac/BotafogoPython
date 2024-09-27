n_alunos = int(input("digite o número de alunos "))
alunos = []

for i in range(n_alunos):
      nome = input("digite o nome do aluno ")
      nota1 = float(input("digite a primeira nota do aluno "))
      nota2 = float(input("digite a segunda nota do aluno "))
      media = (nota1 + nota2) / 2 #desnecessario colocar em float
      resultado = "aprovado" if media >= 6.5 else "reprovado"

      alunos.append(
        {
            "nome": nome,
            "nota1": nota1,
            "nota2": nota2,
            "media": media,  
            "resultado": resultado  
        })  
      
#for i in alunos.items() 

#for i in range(n_alunos):
print(alunos)     
#    print(alunos["nome"],"-", alunos["nota1"],"-",alunos["nota2"],"-",alunos["media"],"-",alunos["resultado"]) 
    



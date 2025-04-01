nota1= float(input("digite a 1 nota: "))
nota2= float(input("digite a 2 nota: "))
nota3= float(input("digite a 3 nota: "))
media= (nota1 + nota2 + nota2) /3
if media >= 7:
    print (f" aluno aprovado com media  {media:.1f}")
else:
   if media<4:
       print(f"aluno REPROVADO com media {media}")
   else:
       print(f"aluno em recuperação com media {media}")









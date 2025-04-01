nome= input("Digite seu nome: ")
idade= int(input("Digite sua idade: "))
salario= float(input("informe seu salario: "))
aumento= float(input("digite a porcetagem do seu aumento: "))
aumentoreal= salario * aumento/100
novosalario= salario + aumentoreal
print (f"Olá {nome}, você tem {idade} anos \n"
       f" e seu salario é {salario: .2f},você recebeu {aumentoreal: .2f} de aumento, seu salario agora é{novosalario: .2f}")






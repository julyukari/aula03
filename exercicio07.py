tipo = input("Digite o tipo abastecido \n"
             "G para Gasolina \n"
             "E para Etanol \n ")
qtdLitros = float(input("quantos litros: "))
valorG = 5.8
valorE = 4.9
if tipo == "g" or tipo == "G" :
    valor = qtdLitros * valorG
elif tipo == "e" or tipo == "E":
    valor = qtdLitros * valorE
else:
    print("tipo de combustivel invalido!")
print(f"voce gastou R${valor:.2f}")

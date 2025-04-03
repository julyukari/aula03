tipo = input("Digite o tipo abastecido \n"
             "G para Gasolina \n"
             "E para Etanol \n ")
qtdLitros = float(input("quantos litros: "))
valorG = 5.8
valorE = 4.9
if tipo == "G" :
    valor = qtdLitros * valorG
else:
    valor = qtdLitros * valorE
    print(f"voce gastou R${valor: .2f}")

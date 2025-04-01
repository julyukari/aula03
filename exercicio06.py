

time1= input("digite o nome do 1 time: ")
gols1= int(input(f"digite a quantidade de gols do {time1}: "))
time2= input("digite o nome do 2 time: ")
gols2= int(input(f"digite a quantidade de gols do {time2}: "))
if gols1==gols2:
    print("EMPATE")
else:
    if gols1>gols2:
        print(f"O {time1} ganhou")
    else:
        print(f"0 {time2}ganhou")

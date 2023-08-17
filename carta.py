dicionario={
    "ki":7400,
    "tecnicas":6600,
    "velocidade":69,
    "transformacao":4
}
User= input("digite uma nova caracteristica: ").lower()
UserValor=int(input("digite um valor para ela: "))
dicionario.update({User:UserValor})
print(dicionario.keys())
print("escolha uma caracteristica: ")
Carac=input().lower()
if Carac in dicionario:
    print(dicionario.keys(1), dicionario.values(1))
else:
    print("nao existe")

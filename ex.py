#ordenado, mutavel, nao permite valores duplicados,


dicionario= {
    "montadora": "ford",
    "modelo": "mustang",
    "ano ": 1964,
    "ano" : 1980
}
# print(dicionario)
print(dicionario["montadora"])
# print(len(dicionario))
# cliente= dict(nome="Pedro", idade = 25, estado="SP")
# print(cliente)
# print(cliente.keys())
# print(cliente.values())
dicionario["ano"]=2000
print(dicionario)
dicionario.update({"montadora":"fiat"})
print(dicionario)
dicionario["cor"]= "prata"
print(dicionario)
pokemons= (
    'charizard', 'fogo',
    'pikachu', 'eletrico',
    'butterfree', 'inseto',
    'jolteon', 'eletrico',
    'ho-oh', 'fogo',
    'genesect', 'inseto',
    'magmar', 'fogo',
    'weedle', 'inseto',
    'zapdos', 'eletrico',
    'flareon', 'fogo',
)

elemento=input('Digite um elemento aqui: ')
elemento.lower()

# for i in pokemons:
#     if i== "fogo" and elemento=="fogo":
#         loc=int(pokemons.index(i))
#         i=loc-1
#         print(pokemons[i])
#     elif elemento == i[1]:
#         print(i[0])
quant=0
for i in range(len(pokemons)):
    if elemento in pokemons[i]:
        print(pokemons[i-1])
        quant+=1
    else:
        print('nao existe')
    break
print(quant)
    
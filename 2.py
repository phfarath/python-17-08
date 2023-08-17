set= {0}
maiorValor=0

Num= input("escolha entre numeros reais ou inteiros: ").lower()

set.remove(0)

while len(set)<10:
            
    if Num =='reais':
        digito=float(input(f"digite um numero dos {Num}: "))
        set.add(digito)
    elif Num == 'inteiros':
        digito=int(input(f"digite um numero dos {Num}: "))
        set.add(digito)
    else:
        print('invalido')
        break
for i in set:
    if maiorValor < i:
        maiorValor=i
print(f'seu maior valor foi: {maiorValor}')       
print(set)
print(len(set))
import random
pokracovat = 'ano'
while pokracovat == 'ano':
    a = random.randint(1,10)
    b = random.randint(1,10)
    rndm = a * b 
    print(f'priklad {a}*{b}')
    zadani = input('zadej vysledek: ')
    if int(zadani) != rndm:
        print('Go study before game')

    else: 
        print('Nice work!')
    pokracovat = input('chces pokracovat? ano/ne: ')
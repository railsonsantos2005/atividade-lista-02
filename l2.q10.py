def cria_lista (numero):
    for nl in range(numero):
        for nc in range(nl):
            print(f'{nl:4}',end='')
        print()

numero = int (input('entre: '))

cria_lista (numero)
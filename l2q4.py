"faça um programa que verifique se uma letra digitada é vogal ou consoante."

palavra = input('digite a letra:').lower()
vogais = ('a', 'e', 'i', 'o', 'u')
if palavra in vogais:
    print ('a letra e vogal')
else:
    print('a letra e consoante')
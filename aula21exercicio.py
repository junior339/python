nome=input('digite um nome:')
idade=input('digite a sua idade:')
if idade and nome:
    print(f'sua idade e de {idade} e seu nome e {nome}')
    print(f'seu nome ivertido e {nome[::-1]}' )
    print(f'a primeira letra do seu nome e {nome[0]}')
    if ' 'in nome:
       print(f'seu nome contem espaços')
    else:
        print('seu nome nao comtem espaços')
    print(f'seu nome tem {len(nome)} letras')  
    print(f'a ultima letra do seu nome e {nome[-1]}')
else:
    print('desculpe voce deixou espaços vazios')
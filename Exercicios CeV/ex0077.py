palavras = ('aprender','programar','linguagem','python','curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro')
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ',end='')
    for letra in range(0,len(palavra)):
        if palavra[letra] in 'aeiou':
            print(f"{palavra[letra]} ", end='')



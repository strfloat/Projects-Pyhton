intro='''
    ####################################################
    ### ISTO É UM CONVERSOR DE SISTEMAS DE NUMERAÇÃO ###
    ####################################################
    '''
print(intro)
bbit=str(input('Qual a base do número? '))
bbit=bbit.upper()

if bbit==('BINARIO') or bbit==('BINÁRIO'):
    bit=str(input('Qual o número binário a converter? '))
    bcbit=str(input('Converter o número binário para qual base? '))
    bcbit=bcbit.upper()
    if bcbit==('DECIMAL'):
        print(int(bit, 2))
    #detetar erro esta a dar números a mais
    if bcbit==('OCTAL'):
        b=int(bit, 2)
        print(oct(b))
    if bcbit==('HEXADECIMAL'):
        b=int(bit, 2)
        print(hex(b))
if bbit==('OCTAL'):
    bit=str(input('Qual o número octal a converter? '))
    bcbit=str(input('Converter o número octal para qual base? '))
    bcbit=bcbit.upper()
    if bcbit==('DECIMAL'):
        print(int(bit, 8))
    #aparece numeros e letras a mais
    if bcbit==('BINARIO') or bcbit==('BINÁRIO'):
        b=int(bit, 8)
        print(bin(b))
    if bcbit==('HEXADECIMAL'):
        b=int(bit, 8)
        print(hex(b))
if bbit==('HEXADECIMAL'):
    bit=str(input('Qual o número hexadecimal a converter? '))
    bcbit=str(input('Converter o número hexadecimal para qual base? '))
    bcbit=bcbit.upper()
    if bcbit==('DECIMAL'):
        print(int(bit, 16))
    if bcbit==('BINARIO') or bcbit==('BINÁRIO'):
        b=int(bit, 16)
        print(bin(b))
    if bcbit==('OCTAL'):
        b=int(bit, 16)
        print(oct(b))
if bbit==('DECIMAL'):
    bit=int(input('Qual o número decimal a converter? '))
    bcbit=str(input('Converter o número decimal para qual base? '))
    bcbit=bcbit.upper()
    if bcbit==('HEXADECIMAL'):
        print(hex(bit))
    if bcbit==('BINARIO') or bcbit==('BINÁRIO'):
        print(bin(bit))
    if bcbit==('OCTAL'):
        print(oct(bit))



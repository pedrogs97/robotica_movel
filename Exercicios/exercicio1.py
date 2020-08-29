'''
Autores: Pedro Gustavo e Vítor Pontes.
Matéria: Robótica Móvel.
Professor: Marco Antonio.
'''
def question1():
    from statistics import median

    count = 0
    arrNumbers = list()
    while count != 3:
        number = input('Digite um numero: ')
        count += 1
        arrNumbers.append(float(number))
    print(median(arrNumbers))

def question3():
    from os import get_terminal_size
    import math

    size = get_terminal_size()
    word = input('Digite uma palavra:')
    len_word = len(word)
    new_string = str()
    count = 0
    pos_new = math.trunc(size.columns/2)
    pos_old = math.trunc(len_word/2)
    pos_new = pos_new - pos_old
    pos_word = 0
    while count != size.columns:
        if (count >= pos_new and pos_word < len_word):
            new_string += word[pos_word]
            pos_word += 1
        else:
            new_string += ' '
        count += 1
   

    print(new_string)

def isInteger():
    number = input('Digite o valor: ')
    number.strip()
    if not number:
        print('False')
        return False
    for c in number:
        if c == '+' or c == '-' :
            continue
        elif c.isspace():
            print('False')
            return False
        elif c.isalpha():
            print('False')
            return False
        elif not c.isalnum():
            print('False')
            return False
    print('True')
    return True

def question8():
    passwd = input('Digite sua senha: ')
    lower = False
    upper = False
    number = False
    char8 = len(passwd) >= 8
    for c in passwd:
        if c.islower():
            lower = True
        elif c.isupper():
            upper = True
        elif c.isnumeric():
            number = True
    if lower and upper and number and char8:
        print('Boa.')
    else:
        print('Fraca.')

def question9():
    def decToOther(new_base, num):
        if new_base == '2':
            print('Convertendo para binário: ')
            print(bin(num))
        elif new_base == '8':
            print('Convertendo para octal: ')
            print(oct(num))
        else:
            print('Convertendo para hexa: ')
            print(hex(num))

    def otherToDec(base, num):
        if base == '2':
            print((int(num,2)))
        elif new_base == '8':
            print(oct(int(num,8)))
        else:
            print(hex(int(num,16)))

    base = input('Base do número de entrada: ')
    new_base = input('Nova base: ')
    number = input('Número a ser convertido: ')
    if base == '10':
        decToOther(new_base, int(number))
    else:
        otherToDec(base, number)
   
def question10():
    from fractions import Fraction

    numerador = input('Numerador: ')
    denominador = input('Denominador: ')
    if int(denominador) == 0 or not numerador or not denominador or not numerador.isnumeric or not denominador.isnumeric:
        print('Inválido.')
        return
    print(Fraction(int(numerador), int(denominador)))

if __name__ == "__main__":
    question1()
    question3()
    isInteger()
    question8()
    question9()
    question10()
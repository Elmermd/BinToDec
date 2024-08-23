
# Convertidor de números binarios en base 2 a números decimales en base 10, y viceversa. 
# El usuario puede decidir hasta cuando terminar las operaciones. 


def comparador(a,b):
    list = []
    for n in range(0,len(a)):
        if a[n] == '1':
            list.append(b[n])
    return list

def entrada():
    wrong = True
    while wrong:
        n = input('Ingresa 1 para convertir de binario a decimal o ingresa 2 para convertir de decimal a binario: ')
        if n not in ['1','2']:
            print("Número no válido, vuelve a intentarlo.")
        else:
            return n

def binario():
    wrong = True
    while wrong:
        bin = input('Ingresa el número binario a convertir: ')
        for digit in bin:
            if digit not in ['0','1']:
                print('La entrada ingresada no corresponde a un número binario, intentalo nuevamente.')
                break
        else:
            return bin
        
def deci_num():
    wrong = True
    while wrong:
        num = input('Ingresa el número decimal a convertir: ')
        if num.isdigit():
            return num
        else:
            print("Entrada inválida. Por favor, ingresa un número entero.")

def salida():
    wrong = True
    while wrong:
        sal = input('Deseas realizar otra operación? (y o n): ')
        if sal not in ['y','Y','n','N']:
            print("Entrada inválida. Por favor, ingresa si (y) o no (n).")
        else:
            return sal


quit = True
while quit:
    n = entrada()

    if int(n) == 1:
        bi = binario()
        len_binario = len(bi)
        list_binario = list(bi)
        bits = []
        max_bit = 1

        for num in range(0,len_binario):
            if num == 0:
                max_bit = 1
            else:
                max_bit=max_bit*2
        while True:
            bits.append(max_bit)
            max_bit = max_bit/2
            if max_bit<1:
                break

        c = comparador(list_binario,bits)
        print('El número binario '+bi + f' en decimal es: {sum(c)}')

        q = salida()
        if q == 'y':
            bits = []
            continue
        elif q == 'n':
            quit = False
            break


    if int(n) == 2:
        decimal = deci_num()
        max_decimal = int(decimal)
        bin_num = []
        while True:
            bin_num.append(max_decimal % 2)
            max_decimal = max_decimal/2
            max_decimal = int(max_decimal)
            if max_decimal == 0:
                break
        conv_bin = bin_num[::-1]
        string_conjunta = ''.join(map(str, conv_bin))
        print('El número decimal '+decimal + ' en binario es: '+string_conjunta)
        #print(conv_bin)

        q = salida()
        if q == 'y':
            continue
        elif q == 'n':
            quit = False
            break

def op(oper, n1, n2):
    if oper == 'suma':
        return n1 + n2
    elif oper == 'resta':
        return n1 - n2
    elif oper == 'multiplicacion':
        return n1 * n2
    
n1 = int(input('ingrese un numero:'))
n2 = int(input('ingrese otro numero:'))
operacion = input('ingrese otro numero:')

print(op(operacion, n1, n2))
    
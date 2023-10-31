def arithmetic(arith: str):
    if '+' in arith:
        arith = arith.split('+')
        return int(arith[0]) + int(arith[1])
    elif '-' in arith:
        arith = arith.split('-')
        return int(arith[0]) - int(arith[1])
    elif '*' in arith:
        arith = arith.split('*')
        return int(arith[0]) * int(arith[1])
    elif '/' in arith:
        arith = arith.split('/')
        return int(arith[0]) / int(arith[1])
    else:
        return 'Your Aritmetic operation have problem!'

proc = input('Import your arithmetic operation ')
print(arithmetic(proc))